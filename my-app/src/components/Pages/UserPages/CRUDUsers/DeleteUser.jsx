import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import DataUsuario from '../../../../data/DataUsuario';  // Asegúrate de que la ruta es correcta

export default function DeleteUser() {
  const [userId, setUserId] = useState('');
  const [usuarios, setUsuarios] = useState(DataUsuario);

  const handleChange = (event) => {
    setUserId(event.target.value);
  };

  const handleDelete = (id) => {
    const updatedUsuarios = usuarios.filter(usuario => usuario.idUser.toString() !== id);
    setUsuarios(updatedUsuarios);
    console.log(`Usuario con ID ${id} ha sido eliminado.`);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    handleDelete(userId);
    setUserId(''); // Limpiar el campo después de enviar
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
      <Typography variant="h6">Delete User</Typography>
      <TextField
        required
        id="user-id"
        label="User ID"
        type="text"
        onChange={handleChange}
        value={userId}
      />
      <Button type="submit" variant="contained" color="error">
        Delete
      </Button>
    </Box>
  );
}
