import React from 'react';
import './UserName.css'
import PropTypes from 'prop-types'

class UserName extends React.Component {
  render(){
    const name = this.props.name
    return(
      <>
        <p>UserName: </p>
        <p className='name'>
          {name}
        </p>
      </>
    );
  }
}

UserName.propTypes = {
  name: PropTypes.string.isRequired,
}

export default UserName;
