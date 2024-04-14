import React from 'react';
import Card from '../../Card/Card';
import { Outlet, useLocation } from 'react-router-dom';
import './Styles.css';
import create from '../../Img/create.jpg';
import read from '../../Img/read.png';
import upd from '../../Img/update.png';
import del from '../../Img/delete.jpeg' ;

const Users = () => {
  const location = useLocation();
  const isUsersRoute = location.pathname === '/users';

  return (
    <div>
      {isUsersRoute && (
        <div className="card-container">
          <Card
            title="Crear Usuario"
            imageSource={create}
            url="create"
            text="Registra un nuevo usuario en el sistema."
          />
          <Card
            title="Listar Usuarios"
            imageSource={read}
            url="read"
            text="Visualiza la lista de usuarios registrados."
          />
          <Card
            title="Actualizar Usuario"
            imageSource={upd}
            url="update"
            text="Edita la información de un usuario existente."
          />
          <Card
            title="Eliminar Usuario"
            imageSource={del}
            url="delete"
            text="Elimina un usuario del sistema."
          />
        </div>
      )}
      <Outlet />
    </div>
  );
};

export default Users;
