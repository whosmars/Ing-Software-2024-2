import './App.css';

import Alumnos from './components/Alumnos/Alumnos';
import NuevoAlumno from './components/NuevoAlumno/NuevoAlumno';

function App() {
  
  const alumnos = [
    {
      "nombre": "Fernando",
      "apellido": "Fong",
      "numCta": 313320679
    },
    {
      "nombre": "Valeria",
      "apellido": "Garcia",
      "numCta": 314006088
    },
    {
      "nombre": "Erick",
      "apellido": "Martinez",
      "numCta": 414890123
    }
  ];

  const agregarAlumno = alumno => {
    console.log("In App.js")
  }

  return (
    <div className="App">
      <NuevoAlumno onAgregarAlumno={agregarAlumno} />
      <Alumnos alumnos={alumnos} /> 
    </div>
  );
}

export default App;
