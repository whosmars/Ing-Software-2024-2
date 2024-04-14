import React from 'react';
import Card from '../../Card/Card';
import { Outlet, useLocation } from 'react-router-dom';
import './Styles.css'; // Asegúrate de que el path es correcto
import create from '../../Img/create.jpg';
import read from '../../Img/read.png';
import upd from '../../Img/update.png';
import del from '../../Img/delete.jpeg' ;

const Movies = () => {

  const location = useLocation();
    const isMoviesRoute = location.pathname === '/movies';

  return (
    <div>
      {isMoviesRoute && (
    <div className="card-container">
    
      <Card
        title="Crear Película"
        imageSource={create}
        url="create"
        text="Añade una nueva película al catálogo."
      />
      <Card
        title="Listar Películas"
        imageSource={read}
        url="read"
        text="Visualiza la lista de películas disponibles."
      />
      <Card
        title="Actualizar Película"
        imageSource={upd}
        url="update"
        text="Actualiza la información de una película existente."
      />
      <Card
        title="Eliminar Película"
        imageSource={del}
        url="delete"
        text="Elimina una película del catálogo."
      />
    </div>
    )}
    <Outlet />
    </div>
  );
};

export default Movies;
