import * as React from 'react';
import { NavLink } from 'react-router-dom';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
import './CardStyles.css';


export default function ActionAreaCard({ title, imageSource, url, text, onSelect }) {

  const handleCardClick = () => {
    if (onSelect) {
      onSelect();
    }
  }

  return (
    <div className="card-container">
    <Card sx={{ maxWidth: 345 }}>
      <NavLink to={url} style={{ textDecoration: 'none' }} onClick={handleCardClick}>
        <CardActionArea>
          <CardMedia
            component="img"
            height="300"
            image={imageSource}
            alt={title}
          />
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              {title}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              {text}
            </Typography>
          </CardContent>
        </CardActionArea>
      </NavLink>
    </Card>
    </div>
  );
}




