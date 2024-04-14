import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import rentalData from '../../data/DataRenta'; 

export default function RentalTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Rental ID</TableCell>
            <TableCell>User ID</TableCell>
            <TableCell>Movie ID</TableCell>
            <TableCell>Rental Date</TableCell>
            <TableCell>Rental Days</TableCell>
            <TableCell>Status</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rentalData.map((rental) => (
            <TableRow
              key={rental.rentalId}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {rental.rentalId}
              </TableCell>
              <TableCell>{rental.userId}</TableCell>
              <TableCell>{rental.movieId}</TableCell>
              <TableCell>{rental.rentalDate ? new Date(rental.rentalDate).toLocaleDateString() : 'N/A'}</TableCell>
              <TableCell>{rental.rentalDays}</TableCell>
              <TableCell>{rental.status ? 'Active' : 'Returned'}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
