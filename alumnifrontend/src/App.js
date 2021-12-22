import React, { useEffect, useState } from "react";
import "./App.css";
import Schools from "./components/home";
import PostLoadingComponent from "./components/postLoading";

function App() {
  const PostLoading = PostLoadingComponent(Schools);
  const [appState, setAppState] = useState({
    loading: false,
    posts: null,
  });

  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = "http://127.0.0.1:8000/alumniapp/school";

    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        setAppState({ loading: false, posts: data });
      });
  }, [setAppState]);
  return (
    <div className="App">
      {/* <h1>Latest users</h1> */}
      <PostLoading isLoading={appState.loading} posts={appState.posts} />
    </div>
  );
}

export default App;
// import React from "react";

// class connectionExample extends React.Component {
//   componentDidMount() {
//     const apiUrl = "http://127.0.0.1:8000/alumniapp/";

//     fetch(apiUrl)
//       .then((response) => response.json())
//       .then((data) => console.log(data))
//       .catch((error) => console.log(error));
//   }
//   render() {
//     return <div>Example connection</div>;
//   }
// }

//export default connectionExample;
