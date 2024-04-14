import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import rentData from '../../../../data/DataRenta'; // Make sure the path is correct

export default function UpdateRent() {
  const [rentId, setRentId] = useState('');
  const [rent, setRent] = useState({
    rentalId: '',
    userId: '',
    movieId: '',
    rentalDate: '',
    rentalDays: '',
    status: false
  });
  const [found, setFound] = useState(false);

  const handleSearchChange = (event) => {
    setRentId(event.target.value);
  };

  const handleSearch = () => {
    const rentToEdit = rentData.find((r) => r.rentalId.toString() === rentId);
    if (rentToEdit) {
      setRent(rentToEdit);
      setFound(true);
    } else {
      alert("Rent not found");
      setFound(false);
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setRent({ ...rent, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle the update logic here, such as an API call
    console.log('Updated rent data:', rent);
  };

  return (
    <Box sx={{ '& .MuiTextField-root': { m: 1 } }}>
      <Box display="flex" alignItems="center">
        <TextField
          required
          label="Rental ID"
          value={rentId}
          onChange={handleSearchChange}
        />
        <Button variant="contained" onClick={handleSearch}>
          Search
        </Button>
      </Box>
      {found && (
        <Box component="form" onSubmit={handleSubmit}>
          <TextField
            name="userId"
            label="User ID"
            type="number"
            value={rent.userId}
            onChange={handleChange}
          />
          <TextField
            name="movieId"
            label="Movie ID"
            type="number"
            value={rent.movieId}
            onChange={handleChange}
          />
          {/* Date picker for rentalDate */}
          <TextField
            name="rentalDate"
            label="Rental Date"
            type="date"
            value={rent.rentalDate}
            onChange={handleChange}
            InputLabelProps={{ shrink: true }}
          />
          <TextField
            name="rentalDays"
            label="Rental Days"
            type="number"
            value={rent.rentalDays}
            onChange={handleChange}
          />
          <Box display="flex" alignItems="center">
            <label>
              Status:
              <select
                name="status"
                value={rent.status ? 'true' : 'false'}
                onChange={handleChange}
              >
                <option value="true">Active</option>
                <option value="false">Returned</option>
              </select>
            </label>
          </Box>
          <Button type="submit" variant="contained" color="primary">
            Update Rent
          </Button>
        </Box>
      )}
    </Box>
  );
}
