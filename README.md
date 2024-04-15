# Ingeniería de Software 2024-2/Practica 4-react
Repositorio oficial de la materia de Ingenieria de Software de la Facultad de Ciencias de la UNAM del semestre 2024-2

## Práctica

Número 4

## Alumno

Rocha Salazar Mario Alberto

## Profesores:

- Francisco Valdes Souto
- Valeria Garcia Landa
- Fernando Fong
- Erick Martínez Piza
- Adriana Hernandez Gasca

## Descripción

Este proyecto es una aplicación desarrollada con React que simula un sistema con operaciones CRUD (Crear, Leer, Actualizar, Borrar) para varias entidades. Cada sección de la aplicación (Usuarios, Películas, Rentas) cuenta con su propio conjunto de operaciones CRUD, excepto Rentas que no incluye todas las operaciones.

## Datos simulados

Los datos utilizados en la aplicación están simulados y se encuentran en la sección `data` del proyecto, representando una imitación de lo que sería un backend. Los datos son estáticos y se encuentran hardcodeados dentro de la aplicación.

## Funcionalidad

Estéticamente, la aplicación está diseñada para ser intuitiva y fácil de usar. Sin embargo, es importante mencionar que la consistencia de los datos no está completamente asegurada para las operaciones de Delete y Update en el momento de realizar una operación de Read. Esto significa que, aunque las funcionalidades para modificar y eliminar están presentes en la interfaz, los cambios pueden no reflejarse de manera persistente en las visualizaciones subsiguientes.

## Estructura de la Practica 


src
├── App
│   └── App.jsx
├── App.css
├── App.js
├── App.test.js
├── components
│   ├── Card
│   │   ├── Card.jsx
│   │   └── CardStyles.css
│   ├── DeleteForm
│   │   └── DeleteForm.jsx
│   ├── Form
│   │   ├── MovieForm.jsx
│   │   ├── RentForm.jsx
│   │   └── UserForm.jsx
│   ├── Img
│   │   ├── create.jpg
│   │   ├── delete.jpeg
│   │   ├── movies.jpg
│   │   ├── read.png
│   │   ├── rents.jpg
│   │   ├── update.png
│   │   └── user.png
│   ├── Pages
│   │   ├── Home
│   │   │   ├── HomePage.jsx
│   │   │   └── Styles.css
│   │   ├── MoviePages
│   │   │   ├── CRUDMovies
│   │   │   │   ├── CreateMovie.jsx
│   │   │   │   ├── DeleteMovie.jsx
│   │   │   │   ├── ReadMovie.jsx
│   │   │   │   └── UpdateMovie.jsx
│   │   │   ├── Movies.jsx
│   │   │   └── Styles.css
│   │   ├── RentPages
│   │   │   ├── CRURents
│   │   │   │   ├── CreateRent.jsx
│   │   │   │   ├── ReadRent.jsx
│   │   │   │   └── UpdateRent.jsx
│   │   │   ├── Rents.jsx
│   │   │   └── Styles.css
│   │   ├── Root
│   │   │   └── Root.jsx
│   │   └── UserPages
│   │       ├── CRUDUsers
│   │       │   ├── CreateUser.jsx
│   │       │   ├── DeleteUser.jsx
│   │       │   ├── ReadUser.jsx
│   │       │   └── UpdateUser.jsx
│   │       ├── Styles.css
│   │       └── Users.jsx
│   └── Table
│       ├── MovieTable.jsx
│       ├── RentTable.jsx
│       └── UserTable.jsx
├── data
│   ├── DataPelicula.js
│   ├── DataRenta.js
│   └── DataUsuario.js
├── index.css
├── index.js
├── logo.svg
├── reportWebVitals.js
└── setupTests.js





