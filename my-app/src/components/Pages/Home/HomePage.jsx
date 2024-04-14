import React from 'react';
import Card from '../../Card/Card';
import './Styles.css'; 
import movies from '../../Img/movies.jpg'; 
import rents from '../../Img/rents.jpg'; 
import users from '../../Img/user.png';

const HomePage = () => {
  return (
    <div className="body-background">
    <div className="card-container">
      <Card
        title="Usuarios"
        imageSource ={users}
        url="/users"
        text="Haz click para ir al CRUD usuarios"
      />
      <Card
        title="Peliculas"
        imageSource={movies}
        url="/movies"
        text="Haz click para ir al CRUD peliculas"
      />
      <Card
        title="Rentas"
        imageSource={rents}
        url="/rents"
        text="Haz click para ir al CRU rentas"
      />
    </div>
    </div>
  );
};

export default HomePage;
