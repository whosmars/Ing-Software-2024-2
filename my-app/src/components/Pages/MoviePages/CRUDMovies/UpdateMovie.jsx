import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import movieData from '../../../../data/DataPelicula'; // Ensure the path is correct

export default function UpdateMovie() {
  const [movieId, setMovieId] = useState('');
  const [movie, setMovie] = useState({
    title: '',
    genre: '',
    duration: '',
    stock: '',
  });
  const [found, setFound] = useState(false);

  const handleSearchChange = (event) => {
    setMovieId(event.target.value);
  };

  const handleSearch = () => {
    const movieToEdit = movieData.find((m) => m.movieId.toString() === movieId);
    if (movieToEdit) {
      setMovie(movieToEdit);
      setFound(true);
    } else {
      alert("Movie not found");
      setFound(false);
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setMovie({ ...movie, [name]: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    //Aqui se manejaría la lógica de actualización en un backend
    console.log('Updated movie data:', movie);
  };

  return (
    <Box sx={{ '& .MuiTextField-root': { m: 1 } }}>
      <Box display="flex" alignItems="center">
        <TextField
          required
          label="Movie ID"
          value={movieId}
          onChange={handleSearchChange}
        />
        <Button variant="contained" onClick={handleSearch}>
          Search
        </Button>
      </Box>
      {found && (
        <Box component="form" onSubmit={handleSubmit}>
          <TextField
            name="title"
            label="Title"
            value={movie.title}
            onChange={handleChange}
          />
          <TextField
            name="genre"
            label="Genre"
            value={movie.genre}
            onChange={handleChange}
          />
          <TextField
            name="duration"
            label="Duration"
            type="number"
            value={movie.duration}
            onChange={handleChange}
          />
          <TextField
            name="stock"
            label="Stock"
            type="number"
            value={movie.stock}
            onChange={handleChange}
          />
          <Button type="submit" variant="contained" color="primary">
            Update Movie
          </Button>
        </Box>
      )}
    </Box>
  );
}
