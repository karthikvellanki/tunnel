import React from "react";
import {
  Icon,
  Button,
  Container,
  Grid,
  Header,
  Image,
  List,
  Segment,
} from "semantic-ui-react";
import { Link } from "react-router-dom";
import { RedocStandalone } from "redoc";

const Docs = () => (
  <React.Fragment>
    <RedocStandalone specUrl="https://petstore.swagger.io/v2/swagger.json" />
  </React.Fragment>
);

export default Docs;
