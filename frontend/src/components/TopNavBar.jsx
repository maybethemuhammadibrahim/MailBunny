/* TopNavBar.jsx
 * ---------------------------------------------------------------
 * Fixed top navigation bar matching the HTML mockup. Sits to
 * the right of the sidebar (offset by 80px). Contains the page
 * title, search bar, notification/help icons, and user avatar.
 * Uses backdrop-blur for a frosted glass effect.
 * --------------------------------------------------------------- */

import { useLocation } from 'react-router-dom';


/**
 * Returns a human-readable page title based on the current route.
 * Used to display the correct heading in the top nav bar.
 *
 * @param {string} pathname — the current URL path (e.g. "/email")
 * @returns {string} the page title to display
 */
function getPageTitle(pathname) {
  // Map each route to its display title
  const titles = {
    '/': 'Dashboard',
    '/email': 'Dashboard',
    '/crafter': 'Dashboard',
    '/orders': 'Dashboard',
    '/settings': 'Dashboard',
  };

  // Return the matching title, or "Dashboard" as fallback
  return titles[pathname] || 'Dashboard';
}


/**
 * TopNavBar is the fixed header bar at the top of the page.
 * It spans from the right edge of the sidebar to the right
 * edge of the viewport. Contains:
 *   - Page title (left)
 *   - Search bar (center-left)
 *   - Notification + Help icons (right)
 *   - User avatar (far right)
 *
 * @returns {JSX.Element} the top navigation bar
 */
function TopNavBar() {
  // Get current path to determine the page title
  const location = useLocation();
  const pageTitle = getPageTitle(location.pathname);

  return (
    <header className="fixed top-0 right-0 w-[calc(100%-80px)] h-16 bg-surface/80 backdrop-blur-md shadow-sm flex justify-between items-center px-[2rem] z-40">

      {/* Left side — page title and search */}
      <div className="flex items-center gap-[1.5rem]">
        {/* Page title */}
        <h1 className="text-[20px] font-semibold leading-[1.3] tracking-[-0.01em] text-on-surface">
          {pageTitle}
        </h1>

        {/* Search bar — pill-shaped input with search icon */}
        <div className="relative hidden md:block w-64 focus-within:ring-2 focus-within:ring-primary/20 rounded-full transition-all duration-200">
          {/* Search icon positioned inside the input */}
          <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">
            search
          </span>

          {/* Search input field */}
          <input
            type="text"
            placeholder="Search..."
            className="w-full bg-surface-container-lowest border border-outline-variant rounded-full py-2 pl-10 pr-4 text-[13px] font-semibold text-on-surface placeholder:text-on-surface-variant focus:outline-none focus:border-primary"
          />
        </div>
      </div>

      {/* Right side — action icons and avatar */}
      <div className="flex items-center gap-2">
        {/* Notifications button */}
        <button className="p-2 text-on-surface-variant hover:text-primary transition-colors rounded-full hover:bg-surface-container-low">
          <span className="material-symbols-outlined">notifications</span>
        </button>

        {/* Help button */}
        <button className="p-2 text-on-surface-variant hover:text-primary transition-colors rounded-full hover:bg-surface-container-low">
          <span className="material-symbols-outlined">help</span>
        </button>

        {/* User avatar — placeholder circle with initials */}
        <div className="h-8 w-8 rounded-full overflow-hidden ml-2 border border-outline-variant bg-surface-container-high flex items-center justify-center">
          <span className="text-[12px] font-semibold text-on-surface-variant">AI</span>
        </div>
      </div>
    </header>
  );
}

export default TopNavBar;
