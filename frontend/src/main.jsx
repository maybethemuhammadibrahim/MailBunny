/* main.jsx
 * ---------------------------------------------------------------
 * React application entry point. Mounts the root App component
 * into the DOM and imports global styles. This is the file that
 * Vite's index.html points to via <script type="module">.
 * --------------------------------------------------------------- */

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

// Find the #root div in index.html and mount our React app into it
const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);

// StrictMode enables extra development warnings for common mistakes
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
