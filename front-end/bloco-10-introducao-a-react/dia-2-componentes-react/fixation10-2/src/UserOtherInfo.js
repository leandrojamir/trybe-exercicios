import React from 'react';
import PropTypes from 'prop-types'

class UserOtherInfo extends React.Component {
  render(){
    const { email, id } = this.props
    return (
      <>
        <p>
            UserOtherInfo
            {email} {id}
        </p>
      </>

    );
  }
}

UserOtherInfo.propTypes = {
  email: PropTypes.string,
  id: PropTypes.number.isRequired,
}

export default UserOtherInfo;