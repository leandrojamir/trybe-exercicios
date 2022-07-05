// arquivo App.js, criado pelo create-react-app, modificado
import React from 'react';
import Order from './Order';
import Table from './Table';
import UserName from './UserName';
import UserOtherInfo from './UserOtherInfo';
import Item from './Item';

class App extends React.Component {
  render() {
    const headphone = {
      id: 102,
      user: "cena@gmail.com",
      product: "Razer Headphone",
      price: {
        value: 99.99,
        currency: "dollars"
      }
    };

    const energyDrink = {
      id: 77,
      user: "cena@gmail.com",
      product: "Monster 500mL",
      price: {
        value: 9.99,
        currency: "dollars"
      }
    };

    return (
      <div className="App">
        <h1> Orders recently created </h1>
        <Order order={headphone} />
        <Order order={energyDrink} />
        <Table />
        <UserName />
        <UserOtherInfo />
        <Item />
         {/*  adicione os componentes aqui */}
      </div>
    );
  }
}

export default App;