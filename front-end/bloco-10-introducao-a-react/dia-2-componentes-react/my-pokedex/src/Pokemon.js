import React from 'react';
import PropTypes from 'prop-types';

class Pokemon extends React.Component {
  render() {
    // const { pokemon: { name, type, averageWeight, image } } = this.props;
    const { nome, tipo, peso, foto } = this.props;
    // Fizemos um map no nosso array de pokemons
    // que vai renderizar o componente Pokemon para cada item do array.
    // Então, recebemos a props "pokemon" que é um objeto do array de pokemons
    // Nesses objetos temos informações como name, type e etc, então
    // desestruturamos essas informações e renderizamos em uma tag HTML,
    // no caso, utilizamos um <p>.

    return (
      <div className="pokemon">
        <div>
          {/* <p>{ name }</p>
          <p>{ type }</p>
          <p>
            {`Average weight: ${averageWeight.value} ${averageWeight.measurementUnit}`}
          </p>
        </div>
        <img src={ image } alt={ `${name} sprite` } /> */}
          <p>{`Nome: ${ nome }`}</p>
          <p>{ tipo }</p>
          <p>
            {`Peso ${peso.value} ${peso.measurementUnit}`}
          </p>
        </div>
        <img src={ foto } alt={ `foto do ${nome}` } />
      </div>
    );
  }
}

Pokemon.propTypes = {
  nome: PropTypes.string.isRequired,
  tipo: PropTypes.string.isRequired,
  peso: PropTypes.shape({
    measurementUnit: PropTypes.string,
    value: PropTypes.number,
  }).isRequired,
  image: PropTypes.string.isRequired,
};

export default Pokemon;