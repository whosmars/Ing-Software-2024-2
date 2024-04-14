import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import Root from '../components/Pages/Root/Root.jsx'; 
import HomePage from '../components/Pages/Home/HomePage.jsx';

import Movies from '../components/Pages/MoviePages/Movies.jsx';
import CreateMovie from '../components/Pages/MoviePages/CRUDMovies/CreateMovie.jsx';
import ReadMovie from '../components/Pages/MoviePages/CRUDMovies/ReadMovie.jsx';
import UpdateMovie from '../components/Pages/MoviePages/CRUDMovies/UpdateMovie.jsx';
import DeleteMovie from '../components/Pages/MoviePages/CRUDMovies/DeleteMovie.jsx';

import Users from '../components/Pages/UserPages/Users.jsx';
import CreateUser from '../components/Pages/UserPages/CRUDUsers/CreateUser.jsx';
import ReadUser from '../components/Pages/UserPages/CRUDUsers/ReadUser.jsx';
import UpdateUser from '../components/Pages/UserPages/CRUDUsers/UpdateUser.jsx';
import DeleteUser from '../components/Pages/UserPages/CRUDUsers/DeleteUser.jsx';

import Rents from '../components/Pages/RentPages/Rents.jsx';
import CreateRent from '../components/Pages/RentPages/CRURents/CreateRent.jsx';
import ReadRent from '../components/Pages/RentPages/CRURents/ReadRent.jsx';
import UpdateRent from '../components/Pages/RentPages/CRURents/UpdateRent.jsx';


function App () {



  const router = createBrowserRouter([
    { 
      path: '/', 
      element: <Root />, 
      children: [
        {path: '/', element: <HomePage/>},
        { path: 'movies', 
          element: <Movies/>,
          children: [
            
          { path: 'create', element: <CreateMovie/> },
          { path: 'read', element: <ReadMovie/> },
          { path: 'update', element: <UpdateMovie/> },
          { path: 'delete', element: <DeleteMovie/> }
        ]
        },
        { path: 'users',
          element: <Users/>,
          children: [
            { path: 'create', element: <CreateUser/> },
            { path: 'read', element: <ReadUser/> },
            { path: 'update', element: <UpdateUser/> },
            { path: 'delete', element: <DeleteUser/> }
          ] 
        },
        { path: 'rents',
          element: <Rents/>,
          children: [
            { path: 'create', element: <CreateRent/> },
            { path: 'read', element: <ReadRent/> },
            { path: 'update', element: <UpdateRent/> }
          ]
        }
      ]
    }
  ]);


  return (
    <RouterProvider router={router}>
      <div>
        <h1>My App</h1>
      </div>
    </RouterProvider>
  );
}

export default App;
