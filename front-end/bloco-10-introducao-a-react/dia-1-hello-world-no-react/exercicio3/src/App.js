import React from 'react';
import Content from './Content';
import Footer from './Footer';
import Header from './Header';
import './App.css'

class App extends React.Component {
  render() {
    return (
      <>
        <Header />
        <Content />
        <Footer />
      </>
    );
  }
}

export default App;
