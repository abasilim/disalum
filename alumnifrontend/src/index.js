import React from "react";
import ReactDOM from "react-dom";
//import * as serviceWorker from "./serviceWorker";
import "./index.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import App from "./App";
import Header from "./components/header";
import Footer from "./components/footer";
import Register from "./components/register";
import SignIn from "./components/login";
import Logout from "./components/logout";
import SingleSet from "./components/singleset";

const routing = (
  <Router>
    <React.StrictMode>
      <Header />
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="/register" component={Register} />
        <Route path="/login" component={SignIn} />
        <Route path="/logout" component={Logout} />
        <Route path="/school/:slug" component={SingleSet} />
      </Switch>
      <Footer />
    </React.StrictMode>
  </Router>
);

ReactDOM.render(routing, document.querySelector("#root"));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
