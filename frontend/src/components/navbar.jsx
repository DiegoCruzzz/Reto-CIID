import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/startups">Startups</Link></li>
        <li><Link to="/technologies">Tecnologías Emergentes</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar