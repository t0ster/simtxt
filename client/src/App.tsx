import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";
import Home from "pages/home";
import Text from "pages/text";
import { Route, Switch } from "react-router-dom";

export const client = new ApolloClient({
  uri: process.env.REACT_APP_GRAPHQL_URI || "http://localhost:8080/graphql",
  cache: new InMemoryCache(),
});

export default function App() {
  return (
    <ApolloProvider client={client}>
      <Switch>
        <Route path="/text/:id">
          <Text />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </ApolloProvider>
  );
}
