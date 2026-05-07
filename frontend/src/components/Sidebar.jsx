/* Sidebar.jsx
 * ---------------------------------------------------------------
 * Fixed left sidebar navigation matching the HTML mockup exactly.
 * 80px wide, white background, with icon-only nav items that show
 * labels below each icon. Active state uses a right border and
 * filled icon variant. Uses Material Symbols Outlined via CDN.
 * --------------------------------------------------------------- */

import { NavLink, useLocation } from 'react-router-dom';


/**
 * NavItem renders a single sidebar navigation button.
 * It highlights the active route with a right border, primary
 * text color, and switches the icon to filled variant.
 *
 * @param {object} props
 * @param {string} props.to — the route path (e.g. "/email")
 * @param {string} props.icon — Material Symbols icon name (e.g. "home")
 * @param {string} props.label — text label below the icon
 * @param {boolean} props.isActive — whether this is the current route
 * @param {string} [props.className] — additional CSS classes
 * @returns {JSX.Element} a sidebar nav button
 */
function NavItem({ to, icon, label, isActive, className = '' }) {
  // When active: filled icon, primary color, right border accent
  // When inactive: outlined icon, muted color, transparent border
  const activeClasses = isActive
    ? 'text-primary border-r-4 border-primary bg-surface-container-low/50'
    : 'text-on-surface-variant border-r-4 border-transparent hover:bg-surface-container-low';

  // The FILL setting controls whether the Material Symbol is outlined (0) or filled (1)
  const iconFill = isActive ? 1 : 0;

  return (
    <NavLink
      to={to}
      className={`
        relative flex flex-col items-center justify-center
        py-3 w-full transition-all duration-200 active:scale-95
        ${activeClasses} ${className}
      `}
    >
      {/* Material Symbols icon — fill changes based on active state */}
      <span
        className="material-symbols-outlined mb-1"
        style={{ fontVariationSettings: `'FILL' ${iconFill}` }}
      >
        {icon}
      </span>

      {/* Label text below the icon */}
      <span className="text-[11px] font-medium leading-[1.2] tracking-[0.02em]">
        {label}
      </span>
    </NavLink>
  );
}


/**
 * Sidebar is the fixed left navigation panel (80px wide).
 * It contains:
 *   - A brand icon at the top (using the cruelty_free Material Symbol)
 *   - Five navigation items (Home, Email, Crafter, Orders, Settings)
 *   - Settings is pushed to the bottom with mt-auto
 *
 * The active nav item is determined by matching the current URL path.
 *
 * @returns {JSX.Element} the sidebar navigation
 */
function Sidebar() {
  // Get the current URL path to determine which nav item is active
  const location = useLocation();
  const currentPath = location.pathname;

  return (
    <aside className="fixed left-0 top-0 h-full w-[80px] bg-surface-container-lowest shadow-sm flex flex-col items-center py-2 z-50">

      {/* Brand / Logo area — uses a decorative icon */}
      <div className="mb-[1.5rem] mt-2">
        <span
          className="material-symbols-outlined text-[32px] font-bold text-primary"
          style={{ fontVariationSettings: "'FILL' 1" }}
        >
          cruelty_free
        </span>
      </div>

      {/* Navigation items — vertical stack */}
      <nav className="flex flex-col gap-2 w-full items-center flex-1 mt-[1.5rem]">
        {/* Home — dashboard */}
        <NavItem
          to="/"
          icon="home"
          label="Home"
          isActive={currentPath === '/'}
        />

        {/* Email — smart inbox */}
        <NavItem
          to="/email"
          icon="mail"
          label="Email"
          isActive={currentPath === '/email'}
        />

        {/* Crafter — AI email composer */}
        <NavItem
          to="/crafter"
          icon="auto_awesome"
          label="Crafter"
          isActive={currentPath === '/crafter'}
        />

        {/* Orders — purchase tracking */}
        <NavItem
          to="/orders"
          icon="shopping_cart"
          label="Orders"
          isActive={currentPath === '/orders'}
        />

        {/* Settings — pushed to bottom of sidebar */}
        <NavItem
          to="/settings"
          icon="settings"
          label="Settings"
          isActive={currentPath === '/settings'}
          className="mt-auto mb-[1.5rem]"
        />
      </nav>
    </aside>
  );
}

export default Sidebar;
