import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import DataPelicula from '../../data/DataPelicula'; // Asegúrate de que la ruta es correcta


export default function MovieForm() {
  // Estado para el formulario con valores iniciales
  const initialState = {
    movieId: '',
    title: '',
    genre: '',
    duration: '',
    stock: '',
  };
  
  const [movie, setMovie] = useState(initialState);

  // Manejador de cambio para los inputs del formulario
  const handleChange = (event) => {
    const { name, value } = event.target;
    setMovie({ ...movie, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    DataPelicula.push(movie);
    // Aquí se manejaría la lógica de envío al backend
    console.log(movie);
    setMovie(initialState);
  };

  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 1, width: '25ch' },
      }}
      noValidate
      autoComplete="off"
      onSubmit={handleSubmit}
    >
      <TextField
        required
        id="movie-id"
        name="movieId"
        label="Movie ID"
        type="number"
        onChange={handleChange}
        value={movie.movieId}
      />
      <TextField
        required
        id="title"
        name="title"
        label="Title"
        onChange={handleChange}
        value={movie.title}
      />
      <TextField
        required
        id="genre"
        name="genre"
        label="Genre"
        onChange={handleChange}
        value={movie.genre}
      />
      <TextField
        required
        id="duration"
        name="duration"
        label="Duration (min)"
        type="number"
        onChange={handleChange}
        value={movie.duration}
      />
      <TextField
        required
        id="stock"
        name="stock"
        label="Stock"
        type="number"
        onChange={handleChange}
        value={movie.stock}
      />
      <Button type="submit" variant="contained" color="primary">
        Add Movie
      </Button>
    </Box>
  );
}
