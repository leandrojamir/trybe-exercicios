import React from 'react';
import Pokemon from './Pokemon';
import pokemons from './data';


class Pokedex extends React.Component {
    render() {
    //   const { pokemons } = this.props;
      // Recebemos do App.js, através da props "pokemons", o nosso array de pokemons.
      // Devemos fazer um map, e nele renderizar o componente <Pokemon>, que receberá
      // por props cada item do array.
      // Lembre-se: é no componente Pokemon que iremos
      // renderizar todas as informações necessárias para a exibição.
        return (
            <div className="pokedex">
                {/* {pokemons.map(pokemon => <Pokemon key={pokemon.id} pokemon={pokemon} />)} */}
              {/* {pokemons.map ((element) => (
                <Pokemon 
                  nome={element.name}
                  tipo={element.type}
                  peso={element.averageWeight}
                  foto={element.image}
                /> */}
              {pokemons.map (({name, type, averageWeight, image}) => (
                <Pokemon 
                  nome={name}
                  tipo={type}
                  peso={averageWeight}
                  foto={image}
                />
              ))}
            </div>
        );
    }
}

export default Pokedex; 