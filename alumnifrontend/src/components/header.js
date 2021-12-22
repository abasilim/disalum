import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import CssBaseline from "@material-ui/core/CssBaseline";
import { makeStyles } from "@material-ui/core/styles";
import { NavLink } from "react-router-dom";
import Link from "@material-ui/core/Link";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles((theme) => ({
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
  },
  link: {
    margin: theme.spacing(1, 1.5),
  },
  toolbarTitle: {
    flexGrow: 1,
  },
  btn: {
    margin: theme.spacing(0, 4, 0, 0),
  },
}));

function Header() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar
        position="static"
        color="primary"
        elevation={0}
        className={classes.appBar}
      >
        <Toolbar className={classes.toobar}>
          <Typography
            variant="h6"
            color="inherit"
            className={classes.toolbarTitle}
          >
            <Link
              component={NavLink}
              to="/"
              underline="none"
              color="textPrimary"
            >
              Alumni
            </Link>
          </Typography>
          <nav>
            <Link
              color="textPrimary"
              href="#"
              className={classes.link}
              component={NavLink}
              to="/register"
            >
              Register
            </Link>
          </nav>
          <Button
            href="/login"
            type="submit"
            variant="contained"
            className={classes.btn}
          >
            Login
          </Button>
          <Button href="logout" type="submit" variant="contained">
            Logout
          </Button>
        </Toolbar>
      </AppBar>
    </React.Fragment>
  );
}

export default Header;
