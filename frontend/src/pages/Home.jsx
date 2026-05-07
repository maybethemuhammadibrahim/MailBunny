/* Home.jsx
 * ---------------------------------------------------------------
 * Dashboard page — displays the user's tasks, upcoming meetings,
 * and email analytics charts. Phase 7 will implement the full
 * layout with live data from the backend API.
 * --------------------------------------------------------------- */


/**
 * Home renders the main dashboard page with three sections:
 *   1. My Tasks — to-do items extracted from emails (left column)
 *   2. Meeting Overview — upcoming meetings (right column, top)
 *   3. Email Analytics — donut chart + legend (right column, bottom)
 *
 * Currently renders placeholder content. Will be connected to
 * GET /todos, GET /meetings, and GET /analytics/overview in Phase 7.
 *
 * @returns {JSX.Element} the dashboard page
 */
function Home() {
  return (
    <div className="flex flex-col gap-[1.5rem]">
      {/* Header section — greeting and New Email button */}
      <div className="flex items-center justify-between mb-2">
        <div>
          <h2 className="text-[32px] font-semibold leading-[1.2] tracking-[-0.02em] text-on-surface mb-1">
            Good evening, Alex.
          </h2>
          <p className="text-[14px] text-on-surface-variant">
            Here is your daily communication breakdown.
          </p>
        </div>

        {/* New Email button */}
        <button className="bg-primary text-on-primary text-[11px] font-medium tracking-[0.02em] py-2 px-6 rounded-full hover:bg-surface-tint transition-colors shadow-sm flex items-center gap-2">
          <span className="material-symbols-outlined text-[16px]">edit</span>
          New Email
        </button>
      </div>

      {/* Dashboard grid — left column (tasks) + right column (meetings + analytics) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-[1.5rem]">

        {/* Left column: My Tasks */}
        <div className="lg:col-span-4 flex flex-col gap-[1.5rem]">
          <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] shadow-sm border border-surface-variant h-full flex flex-col">
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-[20px] font-semibold leading-[1.3] tracking-[-0.01em] text-on-surface">
                My Tasks
              </h3>
              <button className="h-8 w-8 rounded-full bg-surface-container-low text-primary flex items-center justify-center hover:bg-primary hover:text-on-primary transition-colors">
                <span className="material-symbols-outlined">add</span>
              </button>
            </div>
            {/* Placeholder for task items — Phase 7 */}
            <p className="text-[14px] text-on-surface-variant">
              No tasks yet — MailMind will extract to-dos from your emails automatically.
            </p>
          </div>
        </div>

        {/* Right column: Meetings + Analytics */}
        <div className="lg:col-span-8 flex flex-col gap-[1.5rem]">

          {/* Meeting Overview card */}
          <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] shadow-sm border border-surface-variant">
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-[20px] font-semibold leading-[1.3] tracking-[-0.01em] text-on-surface flex items-center gap-2">
                <span className="material-symbols-outlined text-primary">event_note</span>
                Meeting Overview
              </h3>
              <a href="#" className="text-[13px] font-semibold text-primary hover:underline">
                View Calendar
              </a>
            </div>
            {/* Placeholder for meeting cards — Phase 7 */}
            <p className="text-[14px] text-on-surface-variant">
              No upcoming meetings detected yet.
            </p>
          </div>

          {/* Email Analytics card */}
          <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] shadow-sm border border-surface-variant flex-1">
            <h3 className="text-[20px] font-semibold leading-[1.3] tracking-[-0.01em] text-on-surface mb-6 flex items-center gap-2">
              <span className="material-symbols-outlined text-primary">donut_large</span>
              Email Analytics
            </h3>
            {/* Placeholder for charts — Phase 7 */}
            <p className="text-[14px] text-on-surface-variant">
              Analytics will appear here once emails are processed.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
