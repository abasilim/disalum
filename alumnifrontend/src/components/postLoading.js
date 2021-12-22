import Typography from "@material-ui/core/Typography";
import CircularProgress from "@material-ui/core/CircularProgress";
import React from "react";

function PostLoading(Component) {
  return function PostLoadingComponent({ isLoading, ...props }) {
    if (!isLoading) return <Component {...props} />;
    return (
      // A spinner in case of delayed connection to API
      <div>
        <Typography sx={{ display: "flex" }}>
          <CircularProgress disableShrink />
        </Typography>
        <Typography>
          <p style={{ fontSize: "25px" }}>
            We are witing for the data to load!...{" "}
          </p>
        </Typography>
      </div>
    );
  };
}

export default PostLoading;
