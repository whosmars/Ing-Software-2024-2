import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import DataRenta from '../../data/DataRenta';

export default function RentForm() {
  const initialState = {
    rentalId: '',
    userId: '',
    movieId: '',
    rentalDate: '',
    rentalDays: '',
    status: false,
  };

  const [rental, setRental] = useState(initialState);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setRental({ ...rental, [name]: value });
  };

  const handleCheckboxChange = (event) => {
    setRental({ ...rental, status: event.target.checked });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    DataRenta.push(rental);
    console.log(rental);
    setRental(initialState);
  };

  return (
    <Box
      component="form"
      sx={{ '& .MuiTextField-root': { m: 1, width: '25ch' } }}
      noValidate
      autoComplete="off"
      onSubmit={handleSubmit}
    >
      <TextField
        required
        id="rentalId"
        name="rentalId"
        label="Rental ID"
        type="number"
        onChange={handleChange}
        value={rental.rentalId}
      />
      <TextField
        required
        id="userId"
        name="userId"
        label="User ID"
        type="number"
        onChange={handleChange}
        value={rental.userId}
      />
      <TextField
        required
        id="movieId"
        name="movieId"
        label="Movie ID"
        type="number"
        onChange={handleChange}
        value={rental.movieId}
      />
      <TextField
        required
        id="rentalDate"
        name="rentalDate"
        label="Rental Date"
        type="date"
        InputLabelProps={{ shrink: true }}
        onChange={handleChange}
        value={rental.rentalDate}
      />
      <TextField
        required
        id="rentalDays"
        name="rentalDays"
        label="Rental Days"
        type="number"
        onChange={handleChange}
        value={rental.rentalDays}
      />
      <FormControlLabel
        control={
          <Checkbox
            checked={rental.status}
            onChange={handleCheckboxChange}
            name="status"
          />
        }
        label="Status"
      />
      <Button type="submit" variant="contained" color="primary">
        Add Rental
      </Button>
    </Box>
  );
}
