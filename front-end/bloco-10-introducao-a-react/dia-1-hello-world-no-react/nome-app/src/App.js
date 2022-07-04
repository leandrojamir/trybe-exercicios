import React from 'react';
import About from './About';
import HelloJsx from './HelloJsx';
import Hello1 from './Hellow1';
import Hellow2 from './Hellow2';

const Task = (value) => {
  return (
    <li key={value}>{value}</li>
  );
}

const compromissos = ['Acordar', 'Tomar café', 'Escovar os dentes', 'Ir trabalhar'];

class App extends React.Component {
  render() {
    return (
      <>
      <HelloJsx />
      <Hello1 />
      <About />
      <Hellow2 />
      <ul>{ compromissos.map(lista => Task(lista)) }</ul>
    </>
    );
  }
}

export default App;
