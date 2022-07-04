import React from 'react';

class About extends React.Component {
  render() {
    const skills = ["HTML", "CSS", "JS", "Testes unitários"] // adicione mais habilidades aqui
    const jsxSkills = skills.map((skill) => <li>{skill}</li>) // cria um array de tags <li>
    
    return (
      <div>
        <h1>
          {'Leandro Jamir Silva'}
        </h1>
        <p>
          {'Estudante Trybe'}
        </p>
        <h2>Minhas Habilidades</h2>
        <ul>{ jsxSkills }</ul>
      </div>
    );
  }
}

export default About;