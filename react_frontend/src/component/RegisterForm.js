import React from 'react';
import axios from 'axios';
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie'
import jwt from 'jwt-decode';
import { Redirect } from 'react-router-dom';
import { connect, useDispatch } from 'react-redux';
import { set_user } from '../actions';
import "./RegisterForm.css";
import Button from '@mui/material/Button';

// https://reactjs.org/docs/forms.html
class RegisterForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      email: '',
      password: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  static propTypes = {
    cookies: instanceOf(Cookies).isRequired
  };

  handleSubmit(event) {
    const instance = axios.create();
    instance.post('/users/', {
      username: this.state.username,
      email: this.state.email,
      password: this.state.password
    })
      .then((response) => {
        alert("User created successfully")
        const { cookies } = this.props;
        const jwt_token = response.data.access_token
        cookies.set("jwt_token", jwt_token,
          {
            path: "/",
            sameSite: 'strict'
          });
        this.setState({ jwt_token: cookies.get("jwt_token") });
        const user = jwt(jwt_token);
        this.props.signIn(user);
        this.setState({ redirect: '/' });
      })
      .catch(err => {
        alert("Registeration failed")
        alert(JSON.stringify(err.response.data.detail))
      })
    event.preventDefault();
  }


  render() {
    if (this.state.redirect) {
      return <Redirect to={this.state.redirectTo} />
    }
    return (
      <form
        className="registerForm"
        onSubmit={this.handleSubmit}>
        <label className="registerForm__lable">
          Username:
          <span>
            <input
              type="text" name="username" value={this.state.username}
              onChange={this.handleChange} />
          </span>
        </label>
        <label className="registerForm__lable">
          Email:
          <span>
            <input type="email" name="email" value={this.state.email}
              onChange={this.handleChange} />
          </span>
        </label>
        <label>
          Password:
          <span>
            <input type="password" name="password" value={this.state.password}
              onChange={this.handleChange} />
          </span>
        </label>
        <Button type="submit" variant="contained">Register</Button>
      </form>
    )
  }

}


const mapDispatchToProps = (dispatch) => {
  return {
    signIn: (user) => dispatch(set_user(user))
  }
};

export default connect(null, mapDispatchToProps)(withCookies(RegisterForm));
