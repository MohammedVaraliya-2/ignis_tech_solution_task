import { Link } from "react-router-dom";
import { Navbar, Nav, NavDropdown, Button } from "react-bootstrap";
import { useState } from "react";
import logo from "../logo.svg";

function NavbarComponent() {
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogout = () => {
    // logout logic here
    setLoggedIn(false);
  };

  return (
    <Navbar expand="lg" bg="dark" variant="dark">
      <Navbar.Brand as={Link} to="/events">
        <img src={logo} alt="logo" height="30" />
        Events
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link as={Link} to="/">
            Home
          </Nav.Link>
          <Nav.Link as={Link} to="/events">
            Events
          </Nav.Link>
          {loggedIn ? (
            <>
              <Nav.Link as={Link} to="/events/create">
                <Button variant="primary">Create Event</Button>
              </Nav.Link>
              <NavDropdown title="Account" id="basic-nav-dropdown">
                <NavDropdown.Item as={Link} to="/profile">
                  Profile
                </NavDropdown.Item>
                <NavDropdown.Item as={Link} to="/settings">
                  Settings
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item onClick={handleLogout}>
                  Logout
                </NavDropdown.Item>
              </NavDropdown>
            </>
          ) : (
            <>
              <Nav.Link as={Link} to="/register">
                <Button variant="outline-light">Register</Button>
              </Nav.Link>
              <Nav.Link as={Link} to="/login">
                <Button variant="light">Login</Button>
              </Nav.Link>
            </>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavbarComponent;
