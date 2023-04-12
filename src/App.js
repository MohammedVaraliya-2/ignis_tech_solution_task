import React from "react";
import NavbarComponent from "./components/Navbar";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import EventList from "./components/EventList";
import Login from "./components/Login";
import Register from "./components/Register";
import CreateEvent from "./components/CreateEvent";
import IsLikeEvent from "./components/IsLikeEvent";
import Home from "./components/Home";

function App() {
  return (
    <BrowserRouter>
      <NavbarComponent />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/events" element={<EventList />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/events/create" element={<CreateEvent />} />
        <Route path="/events/:id/like" element={<IsLikeEvent />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;