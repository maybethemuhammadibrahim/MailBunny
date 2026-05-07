/* Crafter.jsx
 * ---------------------------------------------------------------
 * AI email composer page. Provides a distraction-free writing
 * view with To/Subject fields, a rich text area, and an AI
 * sidebar for prompt-based generation and tone selection.
 * Phase 9 will implement the full functionality.
 * --------------------------------------------------------------- */


/**
 * Crafter renders the new email composition page. Layout:
 *   - Left: editor canvas with To, Subject, toolbar, and textarea
 *   - Right: AI assistant sidebar with prompt input, tone toggles,
 *     and quick prompt templates
 *
 * Will be connected to POST /crafter/generate and POST /crafter/send
 * in Phase 9.
 *
 * @returns {JSX.Element} the AI email crafter page
 */
function Crafter() {
  return (
    <div className="flex gap-[1.5rem] min-h-[calc(100vh-64px-4rem)]">
      {/* Editor canvas */}
      <div className="flex-1 bg-surface-container-lowest rounded-xl shadow-sm border border-surface-variant p-[1.25rem] flex flex-col">
        {/* Header fields — To and Subject */}
        <div className="flex flex-col gap-4 mb-6 pb-6 border-b border-surface-variant">
          <div className="flex items-center gap-4">
            <label className="w-16 text-[13px] font-semibold text-on-surface-variant uppercase tracking-wider">
              To
            </label>
            <input
              type="text"
              placeholder="Add recipients..."
              className="flex-1 bg-surface-container-lowest border border-outline-variant rounded-lg px-3 py-2 text-[16px] text-on-surface focus:border-primary focus:ring-1 focus:ring-primary transition-all"
            />
          </div>
          <div className="flex items-center gap-4">
            <label className="w-16 text-[13px] font-semibold text-on-surface-variant uppercase tracking-wider">
              Subject
            </label>
            <input
              type="text"
              placeholder="Email subject..."
              className="flex-1 bg-surface-container-lowest border border-outline-variant rounded-lg px-3 py-2 text-[20px] font-semibold text-on-surface focus:border-primary focus:ring-1 focus:ring-primary transition-all"
            />
          </div>
        </div>

        {/* Text editor area */}
        <div className="flex-1 relative flex flex-col">
          <textarea
            className="flex-1 w-full resize-none border-none focus:ring-0 p-0 text-[16px] text-on-surface bg-transparent leading-relaxed outline-none"
            placeholder="Start typing or use AI to craft your message..."
          ></textarea>
        </div>

        {/* Bottom action bar */}
        <div className="mt-6 pt-4 border-t border-surface-variant flex justify-between items-center">
          <button className="text-on-surface-variant hover:text-error transition-colors flex items-center gap-1 text-[13px] font-semibold">
            <span className="material-symbols-outlined text-[18px]">delete</span>
            Discard
          </button>
          <div className="flex gap-3">
            <button className="px-4 py-2 rounded-lg border border-outline-variant text-on-surface hover:bg-surface-container-low transition-colors text-[13px] font-semibold">
              Save Draft
            </button>
            <button className="px-6 py-2 rounded-lg bg-on-surface text-surface-container-lowest hover:bg-on-surface/90 transition-colors text-[13px] font-semibold flex items-center gap-2">
              Send
              <span className="material-symbols-outlined text-[16px]">send</span>
            </button>
          </div>
        </div>
      </div>

      {/* AI assistant sidebar */}
      <aside className="w-80 flex flex-col gap-[1.5rem] shrink-0">
        {/* AI Prompt Input */}
        <div className="bg-surface-container-low rounded-xl p-[1.25rem] border border-surface-variant shadow-sm">
          <h3 className="text-[20px] font-semibold text-on-surface mb-3 flex items-center gap-2">
            <span
              className="material-symbols-outlined text-[20px] text-primary"
              style={{ fontVariationSettings: "'FILL' 1" }}
            >
              auto_awesome
            </span>
            AI Writer
          </h3>
          <p className="text-[14px] text-on-surface-variant mb-4">
            Briefly describe what you want to say, and let the AI draft it for you.
          </p>
          <textarea
            className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg p-3 text-[14px] focus:border-primary focus:ring-1 focus:ring-primary transition-all resize-none h-24 mb-3 text-on-surface"
            placeholder="e.g., Ask Alex for an update on the Q3 report..."
          ></textarea>
          <button className="w-full bg-primary text-on-primary py-2.5 rounded-lg text-[13px] font-semibold hover:bg-surface-tint transition-colors flex justify-center items-center gap-2">
            Generate Draft
            <span className="material-symbols-outlined text-[16px]">arrow_forward</span>
          </button>
        </div>

        {/* Tone selector */}
        <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] border border-surface-variant shadow-sm">
          <h4 className="text-[13px] font-semibold text-on-surface-variant uppercase tracking-wider mb-4">
            Tone & Style
          </h4>
          <div className="flex flex-wrap gap-2">
            <button className="px-3 py-1.5 rounded-full border border-primary bg-primary/10 text-primary text-[14px]">
              Professional
            </button>
            <button className="px-3 py-1.5 rounded-full border border-outline-variant text-on-surface-variant text-[14px] hover:bg-surface-container-low transition-colors">
              Casual
            </button>
            <button className="px-3 py-1.5 rounded-full border border-outline-variant text-on-surface-variant text-[14px] hover:bg-surface-container-low transition-colors">
              Direct
            </button>
            <button className="px-3 py-1.5 rounded-full border border-outline-variant text-on-surface-variant text-[14px] hover:bg-surface-container-low transition-colors">
              Persuasive
            </button>
          </div>
        </div>

        {/* Quick prompts placeholder */}
        <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] border border-surface-variant shadow-sm flex-1">
          <h4 className="text-[13px] font-semibold text-on-surface-variant uppercase tracking-wider mb-4">
            Quick Prompts
          </h4>
          <p className="text-[14px] text-on-surface-variant">
            Quick prompt templates coming in Phase 9.
          </p>
        </div>
      </aside>
    </div>
  );
}

export default Crafter;
