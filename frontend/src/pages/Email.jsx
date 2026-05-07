/* Email.jsx
 * ---------------------------------------------------------------
 * Smart inbox page with a three-pane layout: folder list (left),
 * email list (center), and email detail + AI draft (right).
 * Phase 8 will implement the full functionality with live data.
 * --------------------------------------------------------------- */


/**
 * Email renders the smart inbox page. The three-pane layout:
 *   1. Left pane — folder tabs (Important, All, Drafts, Spam)
 *   2. Center pane — scrollable email list with AI summary previews
 *   3. Right pane — selected email body + AI Draft assistant panel
 *
 * Will be connected to GET /emails/unread and POST /draft in Phase 8.
 *
 * @returns {JSX.Element} the email inbox page
 */
function Email() {
  return (
    <div className="flex gap-[1.5rem] h-[calc(100vh-64px-4rem)]">
      {/* Left pane — Email list */}
      <section className="w-80 shrink-0 flex flex-col bg-surface-container-lowest rounded-xl border border-surface-dim shadow-[0px_4px_20px_rgba(0,0,0,0.03)] overflow-hidden">
        {/* Tabs */}
        <div className="flex border-b border-surface-dim px-4 pt-2">
          <button className="px-4 py-3 text-[13px] font-semibold text-primary border-b-2 border-primary">
            Important
          </button>
          <button className="px-4 py-3 text-[13px] font-semibold text-on-surface-variant hover:text-on-surface transition-colors">
            All
          </button>
        </div>
        {/* Email list placeholder */}
        <div className="flex-1 overflow-y-auto p-4">
          <p className="text-[14px] text-on-surface-variant">
            Connect Gmail to see your emails here (Phase 8).
          </p>
        </div>
      </section>

      {/* Center pane — Email detail */}
      <section className="flex-1 flex flex-col bg-surface-container-lowest rounded-xl border border-surface-dim shadow-[0px_4px_20px_rgba(0,0,0,0.03)] overflow-hidden">
        <div className="flex-1 flex items-center justify-center">
          <p className="text-[14px] text-on-surface-variant">
            Select an email to view its content.
          </p>
        </div>
      </section>

      {/* Right pane — AI Draft */}
      <section className="w-80 shrink-0 flex flex-col bg-surface-container-lowest rounded-xl border border-surface-dim shadow-[0px_4px_20px_rgba(0,0,0,0.03)] overflow-hidden relative">
        {/* Gradient top accent */}
        <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-secondary-container via-primary to-primary-container"></div>
        {/* AI header */}
        <div className="flex items-center gap-3 p-4 border-b border-surface-dim bg-primary-fixed/30 mt-1">
          <div className="h-8 w-8 rounded-full bg-primary text-on-primary flex items-center justify-center">
            <span className="material-symbols-outlined text-[18px]">auto_awesome</span>
          </div>
          <span className="text-[16px] font-semibold text-on-primary-fixed">
            AI Draft Assistant
          </span>
        </div>
        <div className="flex-1 flex items-center justify-center p-4">
          <p className="text-[14px] text-on-surface-variant text-center">
            AI drafts will appear here when you select an email (Phase 8).
          </p>
        </div>
      </section>
    </div>
  );
}

export default Email;
