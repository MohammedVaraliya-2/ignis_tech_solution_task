import React, { useState, useEffect } from "react";
import axios from "axios";

function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    async function fetchEvents() {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.get("http://localhost:8000/events/", {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        setEvents(response.data);
        console.log([events]);
      } catch (error) {
        console.error(error);
      }
    }
    fetchEvents();
  }, []);

  return (
    <div>
      {events.map((event) => (
        <div key={event.id}>
          <h2>{event.event_name}</h2>
          <p>{event.date}</p>
          <img src={event.image_url} alt={event.event_name} />
          <p>{event.is_liked ? 'Liked' : 'unlike'}</p>
        </div>
      ))}
    </div>
  );
}

export default EventList;
