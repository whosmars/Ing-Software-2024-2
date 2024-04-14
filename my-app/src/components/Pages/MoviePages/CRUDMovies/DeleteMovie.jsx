import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import DataPelicula from '../../../../data/DataPelicula';

export default function DeleteMovie() {
  const [movieId, setMovieId] = useState('');
  const [peliculas, setPeliculas] = useState(DataPelicula);

  const handleChange = (event) => {
    setMovieId(event.target.value);
  };

  const handleDelete = (id) => {
    const updatedPeliculas = peliculas.filter(pelicula => pelicula.movieId.toString() !== id);
    setPeliculas(updatedPeliculas);
    console.log(`Película con ID ${id} ha sido eliminada.`);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    handleDelete(movieId);
    setMovieId(''); // Limpiar el campo después de enviar
  };

  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 1, width: '25ch' },
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
      noValidate
      autoComplete="off"
      onSubmit={handleSubmit}
    >
      <Typography variant="h6">Delete Movie</Typography>
      <TextField
        required
        id="movie-id"
        label="Movie ID"
        type="number"
        onChange={handleChange}
        value={movieId}
      />
      <Button type="submit" variant="contained" color="error">
        Delete
      </Button>
    </Box>
  );
}
