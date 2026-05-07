/* App.jsx
 * ---------------------------------------------------------------
 * Root layout component for MailMind. Sets up React Router with
 * five routes and wraps every page in a shared layout that
 * includes the Sidebar (left) and TopNavBar (top).
 * --------------------------------------------------------------- */

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar.jsx';
import TopNavBar from './components/TopNavBar.jsx';
import Home from './pages/Home.jsx';
import Email from './pages/Email.jsx';
import Crafter from './pages/Crafter.jsx';
import Orders from './pages/Orders.jsx';
import Settings from './pages/Settings.jsx';


/**
 * Layout wraps every page with the fixed Sidebar on the left
 * and the TopNavBar at the top. The children (page content)
 * are rendered in the remaining space to the right and below.
 *
 * @param {object} props
 * @param {React.ReactNode} props.children — the current page component
 * @returns {JSX.Element} the shared layout shell
 */
function Layout({ children }) {
  return (
    <div className="min-h-screen bg-surface-bright text-on-surface font-sans">
      {/* Fixed sidebar — always visible on the left */}
      <Sidebar />

      {/* Fixed top navigation bar */}
      <TopNavBar />

      {/* Main content area — offset by sidebar width (80px) and header height (64px) */}
      <main className="ml-[80px] mt-[64px] p-[2rem]">
        {children}
      </main>
    </div>
  );
}


/**
 * App is the root component. It sets up the browser router and
 * defines all five page routes. Every route is wrapped in the
 * Layout component so the sidebar and top bar persist across
 * page navigation.
 *
 * Routes:
 *   /          → Home (dashboard with tasks, meetings, analytics)
 *   /email     → Email (smart inbox with AI drafts)
 *   /crafter   → Crafter (AI email composer)
 *   /orders    → Orders (purchase tracking)
 *   /settings  → Settings (preferences and account)
 *
 * @returns {JSX.Element} the full app with routing
 */
function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          {/* Dashboard — shows tasks, meetings, and email analytics */}
          <Route path="/" element={<Home />} />

          {/* Smart inbox — three-pane email view with AI drafts */}
          <Route path="/email" element={<Email />} />

          {/* AI email composer — write new emails with AI assistance */}
          <Route path="/crafter" element={<Crafter />} />

          {/* Order tracking — view purchases detected from emails */}
          <Route path="/orders" element={<Orders />} />

          {/* Settings — AI preferences, account, and security */}
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
