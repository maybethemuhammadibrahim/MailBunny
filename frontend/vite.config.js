/* vite.config.js
 * ---------------------------------------------------------------
 * Vite build configuration for the MailMind frontend.
 * Registers the React plugin (for JSX support) and the Tailwind
 * CSS v4 plugin (for utility class processing).
 * --------------------------------------------------------------- */

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [
    react(),          // Enables JSX transformation and React fast-refresh
    tailwindcss(),    // Processes Tailwind CSS v4 utility classes
  ],
});
