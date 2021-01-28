import { render, screen } from "@testing-library/react";
import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { Provider } from "rendition";
import App from "./App";

test("renders learn react link", () => {
  render(
    <Provider>
      <Router>
        <App />
      </Router>
    </Provider>
  );
  const linkElement = screen.getByText(/Add Text/i);
  expect(linkElement).toBeInTheDocument();
});
