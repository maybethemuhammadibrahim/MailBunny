/* api/index.js
 * ---------------------------------------------------------------
 * Centralised API wrapper for all frontend-to-backend requests.
 * Every component imports from here instead of calling fetch()
 * directly. This makes it easy to change the base URL, add
 * auth headers, or switch to a different HTTP library later.
 * --------------------------------------------------------------- */

// Base URL for the FastAPI backend — must match the uvicorn server
const API_BASE = 'http://localhost:8000';


/**
 * Makes a GET request to the backend API and returns the JSON response.
 * Wraps fetch() with error handling and prints helpful error messages.
 *
 * @param {string} endpoint — the API path (e.g. "/todos")
 * @returns {Promise<object>} the parsed JSON response
 */
export async function apiGet(endpoint) {
  try {
    // Build the full URL by combining base + endpoint
    const url = `${API_BASE}${endpoint}`;
    const response = await fetch(url);

    // Check if the server returned an error status code
    if (!response.ok) {
      console.error(`[API] GET ${endpoint} failed with status ${response.status}`);
      return null;
    }

    // Parse and return the JSON body
    const data = await response.json();
    return data;

  } catch (error) {
    // Network errors, DNS failures, server down, etc.
    console.error(`[API] GET ${endpoint} error:`, error.message);
    return null;
  }
}


/**
 * Makes a POST request to the backend API with a JSON body.
 * Used for creating resources and triggering AI pipeline actions.
 *
 * @param {string} endpoint — the API path (e.g. "/classify")
 * @param {object} body — the request body to send as JSON
 * @returns {Promise<object>} the parsed JSON response
 */
export async function apiPost(endpoint, body) {
  try {
    const url = `${API_BASE}${endpoint}`;
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      console.error(`[API] POST ${endpoint} failed with status ${response.status}`);
      return null;
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error(`[API] POST ${endpoint} error:`, error.message);
    return null;
  }
}


/**
 * Makes a PATCH request to the backend API. Used for partial
 * updates like marking a todo as done.
 *
 * @param {string} endpoint — the API path (e.g. "/todos/1/done")
 * @param {object} [body] — optional request body
 * @returns {Promise<object>} the parsed JSON response
 */
export async function apiPatch(endpoint, body = {}) {
  try {
    const url = `${API_BASE}${endpoint}`;
    const response = await fetch(url, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      console.error(`[API] PATCH ${endpoint} failed with status ${response.status}`);
      return null;
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error(`[API] PATCH ${endpoint} error:`, error.message);
    return null;
  }
}


/**
 * Makes a DELETE request to the backend API. Used for destructive
 * actions like wiping the database.
 *
 * @param {string} endpoint — the API path (e.g. "/settings/data")
 * @returns {Promise<object>} the parsed JSON response
 */
export async function apiDelete(endpoint) {
  try {
    const url = `${API_BASE}${endpoint}`;
    const response = await fetch(url, {
      method: 'DELETE',
    });

    if (!response.ok) {
      console.error(`[API] DELETE ${endpoint} failed with status ${response.status}`);
      return null;
    }

    const data = await response.json();
    return data;

  } catch (error) {
    console.error(`[API] DELETE ${endpoint} error:`, error.message);
    return null;
  }
}
