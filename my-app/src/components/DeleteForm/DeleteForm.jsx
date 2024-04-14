import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function DeleteResourceForm({ resourceName, onDelete }) {
  const [resourceId, setResourceId] = useState('');

  const handleChange = (event) => {
    setResourceId(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onDelete(resourceId);
    setResourceId('');
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
      <Typography variant="h6">Delete {resourceName}</Typography>
      <TextField
        required
        id={`delete-${resourceName}-id`}
        label={`${resourceName} ID`}
        type="text"
        onChange={handleChange}
        value={resourceId}
      />
      <Button type="submit" variant="contained" color="error">
        Delete
      </Button>
    </Box>
  );
}
