import React from "react";
import { Route, Redirect } from "react-router-dom";
import Hoc from "./hoc/hoc";
import Login from "./containers/Login";
import Signup from "./containers/Signup";
import LandingPage from "./containers/LandingPage";
import Docs from "./containers/Docs";
import ChangeEmail from "./containers/Account/ChangeEmail";
import ChangePassword from "./containers/Account/ChangePassword";
import APIKey from "./containers/Account/APIKey";

const PrivateRoute = ({ component: Component, ...rest }) => {
  const authenticated = localStorage.getItem("token") !== null;
  return (
    <Route
      {...rest}
      render={(props) =>
        authenticated === true ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: props.location },
            }}
          />
        )
      }
    />
  );
};

const BaseRouter = () => (
  <Hoc>
    <Route exact path="/" component={LandingPage} />
    <Route exact path="/docs" component={Docs} />
    <Route path="/login" component={Login} />
    <Route path="/signup" component={Signup} />
    <PrivateRoute path="/account/change-email" component={ChangeEmail} />
    <PrivateRoute path="/account/change-password" component={ChangePassword} />
    <PrivateRoute path="/account/api-key" component={APIKey} />
  </Hoc>
);

export default BaseRouter;
