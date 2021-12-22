import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import Link from "@material-ui/core/Link";
//import SearchBar from "material-ui-search-bar";
import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  card: {
    marginTop: theme.spacing(5),
  },
  cardMedia: {
    paddingTop: "56.25%", //16.9
  },
  link: {
    margin: theme.spacing(1, 1.5),
  },
  cardHeader: {
    backgroundColor:
      theme.palette.type === "light"
        ? theme.palette.grey[200]
        : theme.palette.grey[700],
  },
  userName: {
    fontSize: "16px",
    textAlign: "left",
  },
  userFirstName: {
    display: "flex",
    justifyContent: "left",
    alignItems: "baseline",
    fontSize: "12px",
    textAlign: "left",
    marginBottom: theme.spacing(2),
  },
}));

const Schools = (props) => {
  const { posts } = props;
  const classes = useStyles();
  // new
  let history = useHistory();
  const [data, setData] = useState({ search: "" });

  const goSearch = (e) => {
    history.push({
      pathname: "/search/",
      search: "?search=" + data.search,
    });
    window.location.reload();
  };
  // end new
  if (!posts || posts.length === 0) return <p>Cannot find any user, sorry!</p>;
  return (
    <React.Fragment>
      <Container maxWidth="md" component="main">
        <Grid container spacing={5} alignItems="flex-end">
          {posts.map((user) => {
            return (
              //Enterprise card is full width at sm breakpoint
              <Grid item key={user.id} xs={12} md={4}>
                <Card className={classes.card}>
                  <Link
                    color="textPrimary"
                    href={"/school/" + user.slug}
                    className={classes.link}
                  >
                    <CardMedia
                      className={classes.cardMedia}
                      image="https://source.unsplash.com/random"
                      title="Image"
                    />
                  </Link>
                  <CardContent className={classes.cardContent}>
                    <Typography
                      gutterBottom
                      variant="h6"
                      component="h2"
                      className={classes.userName}
                    >
                      {user.school_name.substr(0, 25)}...
                    </Typography>
                    <div className={classes.userFirstName}>
                      <Typography
                        component="p"
                        color="textPrimary"
                      ></Typography>
                      <Typography variant="p" color="textSecondary">
                        {user.alumni_Name.substr(0, 60)}...
                      </Typography>
                    </div>
                  </CardContent>
                </Card>
              </Grid>
            );
          })}
        </Grid>

        {/* <SearchBar
          value={data.search}
          onChange={(newValue) => setData({ search: newValue })}
          onRequestSearch={() => goSearch(data.search)}
        /> */}
      </Container>
    </React.Fragment>
  );
};

export default Schools;
