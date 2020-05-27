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

const HomepageLayout = () => (
  <React.Fragment>
    <Segment style={{ padding: "8em 0em" }} vertical>
      <Grid container stackable verticalAlign="middle">
        <Grid.Row>
          <Grid.Column width={8}>
            <Header as="h3" style={{ fontSize: "2em" }}>
              Developer portal & API gateway solution
            </Header>
            <p style={{ fontSize: "1.33em" }}>
              Open up your APIs to the world by just adding your endpoints and
              swagger file. Tunnel takes care of provisioning API tokens,
              tracking requests and acting as an API gateway.
            </p>
          </Grid.Column>
          <Grid.Column floated="right" width={6}>
            <Image rounded size="large" src={"static/django-react.jpg"} />
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Segment>
    <Segment style={{ padding: "8em 0em" }} vertical>
      <Grid container stackable verticalAlign="middle">
        <Grid.Row>
          <Grid.Column width={8}>
            <Header as="h3" style={{ fontSize: "2em" }}>
              Integrated User Authentication System
            </Header>
            <p style={{ fontSize: "1.33em" }}>
              User authentication system that allows users to view their API
              token and change their email and password.
            </p>
          </Grid.Column>
          <Grid.Column floated="right" width={6}>
            <Image
              bordered
              rounded
              size="large"
              src={"static/user-authentication.png"}
            />
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Segment>
  </React.Fragment>
);

export default HomepageLayout;
