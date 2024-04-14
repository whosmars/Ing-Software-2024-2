import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Checkbox from '@mui/material/Checkbox';
import DataUsuario from '../../data/DataUsuario'; // Asegúrate de que la ruta es correcta

export default function UserForm() {
  // Estado para el formulario con valores iniciales
  const initialState = {
    idUser: '',
    name: '',
    lastName: '',
    middleName: '',
    password: '',
    email: '',
    profilePicture: '',
    superUser: false,
  };
  
  const [user, setUser] = useState(initialState);

  // Manejador de cambio para los inputs del formulario
  const handleChange = (event) => {
    const { name, value } = event.target;
    setUser({ ...user, [name]: value });
  };

  // Manejador para el checkbox del superusuario
  const handleCheckboxChange = (event) => {
    setUser({ ...user, superUser: event.target.checked });
  };

  // Manejador para el envío del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    DataUsuario.push(user);
    console.log(user);
    setUser(initialState);
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
        id="idUser"
        name="idUser"
        label="User ID"
        type="number"
        onChange={handleChange}
        value={user.idUser}
      />
      <TextField
        required
        id="name"
        name="name"
        label="Name"
        onChange={handleChange}
        value={user.name}
      />
      <TextField
        required
        id="lastName"
        name="lastName"
        label="Last Name"
        onChange={handleChange}
        value={user.lastName}
      />
      <TextField
        id="middleName"
        name="middleName"
        label="Middle Name"
        onChange={handleChange}
        value={user.middleName}
      />
      <TextField
        required
        id="password"
        name="password"
        label="Password"
        type="password"
        autoComplete="new-password"
        onChange={handleChange}
        value={user.password}
      />
      <TextField
        required
        id="email"
        name="email"
        label="Email"
        type="email"
        onChange={handleChange}
        value={user.email}
      />
      <TextField
        id="profilePicture"
        name="profilePicture"
        label="Profile Picture URL"
        onChange={handleChange}
        value={user.profilePicture}
      />
      <Box sx={{ display: 'flex', alignItems: 'center', ml: 1, mb: 2 }}>
        <label htmlFor="superUser">Super User</label>
        <Checkbox
          id="superUser"
          name="superUser"
          checked={user.superUser}
          onChange={handleCheckboxChange}
        />
      </Box>
      <Button type="submit" variant="contained" color="primary">
        Add User
      </Button>
    </Box>
  );
}
