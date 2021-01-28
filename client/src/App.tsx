import { ApolloClient, ApolloProvider, InMemoryCache } from "@apollo/client";
import Home from "pages/home";
import Text from "pages/text";
import { Route, Switch } from "react-router-dom";

// const typeDefs = gql`
//   type Query {
//     texts: [Text!]!
//     text(id: ID!): Text!
//   }
//
//   type Text {
//     id: ID!
//     content: String!
//     sentences: [Sentence!]!
//   }
//
//   type Sentence {
//     id: ID!
//     textId: ID!
//     content: String!
//     similar: [SimilarSentence!]!
//   }
//
//   type SimilarSentence {
//     sentence: Sentence!
//     score: Float!
//   }
// `;
//
// const TEXTS = [
//   {
//     id: "78day78sd",
//     content:
//       "Big white rabbit jumped on a log. Fat crazy fox was chasing for a rabbit. Big white rabbit jumped on a log. Fat crazy fox was chasing for a rabbit. Big white rabbit jumped on a log. Fat crazy fox was chasing for a rabbit. Big white rabbit jumped on a log. Fat crazy fox was chasing for a rabbit.",
//     sentences: [
//       {
//         id: "d8sad123s",
//         textId: "78day78sd",
//         content: "Big white rabbit jumped on a log.",
//         similar: [
//           {
//             sentence: {
//               id: "123dc3",
//               textId: "8dasysdd",
//               content: "Little bear likes strawberries.",
//               similar: [],
//             },
//             score: 0.85,
//           },
//         ],
//       },
//       {
//         id: "hel13d4",
//         textId: "78day78sd",
//         content: "Fat crazy fox was chasing for a rabbit.",
//         similar: [],
//       },
//     ],
//   },
//   {
//     id: "8dasysdd",
//     content: "Little bear likes strawberries. Crazy squirrel likes go nuts.",
//     sentences: [
//       {
//         id: "123dc3",
//         textId: "8dasysdd",
//         content: "Little bear likes strawberries.",
//         similar: [],
//       },
//       {
//         id: "c4ddaf8d",
//         textId: "8dasysdd",
//         content: "Crazy squirrel likes go nuts.",
//         similar: [],
//       },
//     ],
//   },
// ];

// const resolvers = {
//   Query: {
//     texts() {
//       console.log("Fetching texts");
//       return TEXTS;
//     },
//     text(_: any, { id }: any) {
//       return TEXTS.find((t) => t.id === id);
//     },
//   },
// };

// const schema = makeExecutableSchema({ typeDefs, resolvers });

export const client = new ApolloClient({
  uri: process.env.REACT_APP_GRAPHQL_URI || "http://localhost:8080/graphql",
  cache: new InMemoryCache(),
  // @ts-ignore
  // link: new SchemaLink({ schema }),
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
