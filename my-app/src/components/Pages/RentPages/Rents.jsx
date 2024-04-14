import React from 'react';
import Card from '../../Card/Card';
import { Outlet, useLocation } from 'react-router-dom';
import './Styles.css'; // Asegúrate de que el path es correcto
import create from '../../Img/create.jpg';
import read from '../../Img/read.png';
import upd from '../../Img/update.png';

const Rents = () => {
  const location = useLocation();
  const isRentsRoute = location.pathname === '/rents';

  return (
    <div>
      {isRentsRoute && (
        <div className="card-container">
          <Card
            title="Crear Renta"
            imageSource={create}
            url="create"
            text="Registra una nueva renta de película."
          />
          <Card
            title="Listar Rentas"
            imageSource={read}
            url="read"
            text="Visualiza el historial de rentas."
          />
          <Card
            title="Actualizar Renta"
            imageSource={upd}
            url="update"
            text="Actualiza los detalles de una renta."
          />
        </div>
      )}
      <Outlet />
    </div>
  );
};

export default Rents;
