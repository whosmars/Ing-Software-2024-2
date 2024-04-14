import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import userData from '../../../../data/DataUsuario';

export default function UpdateUser() {
  const [userId, setUserId] = useState('');
  const [user, setUser] = useState({
    name: '',
    lastName: '',
    middleName: '',
    password: '',
    email: '',
    profilePicture: '',
    superUser: false
  });
  const [found, setFound] = useState(false);

  const handleSearchChange = (event) => {
    setUserId(event.target.value);
  };

  const handleSearch = () => {
    const userToEdit = userData.find((u) => u.idUser.toString() === userId);
    if (userToEdit) {
      setUser(userToEdit);
      setFound(true);
    } else {
      alert("User not found");
      setFound(false);
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUser({ ...user, [name]: value });
  };

  const handleCheckboxChange = (event) => {
    setUser({ ...user, superUser: event.target.checked });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    //Logica de backend
    console.log('Updated user data:', user);
  };

  return (
    <Box sx={{ '& .MuiTextField-root': { m: 1 } }}>
      <Box display="flex" alignItems="center">
        <TextField
          required
          label="User ID"
          value={userId}
          onChange={handleSearchChange}
        />
        <Button variant="contained" onClick={handleSearch}>
          Search
        </Button>
      </Box>
      {found && (
        <Box component="form" onSubmit={handleSubmit}>
          <TextField
            name="name"
            label="Name"
            value={user.name}
            onChange={handleChange}
          />
          <TextField
            name="lastName"
            label="Last Name"
            value={user.lastName}
            onChange={handleChange}
          />
          <TextField
            name="middleName"
            label="Middle Name"
            value={user.middleName}
            onChange={handleChange}
          />
          <TextField
            name="password"
            label="Password"
            type="password"
            value={user.password}
            onChange={handleChange}
          />
          <TextField
            name="email"
            label="Email"
            type="email"
            value={user.email}
            onChange={handleChange}
          />
          {/* Assuming profilePicture is a URL */}
          <TextField
            name="profilePicture"
            label="Profile Picture URL"
            value={user.profilePicture}
            onChange={handleChange}
          />
          <Box display="flex" alignItems="center">
            <TextField
              name="superUser"
              label="Super User"
              type="checkbox"
              checked={user.superUser}
              onChange={handleCheckboxChange}
            />
          </Box>
          <Button type="submit" variant="contained" color="primary">
            Update User
          </Button>
        </Box>
      )}
    </Box>
  );
}
