/* Settings.jsx
 * ---------------------------------------------------------------
 * Settings page with three sections: AI Preferences (tone,
 * auto-drafting, vocabulary), Account Profile, and Security.
 * Phase 11 will implement the full functionality with live data.
 * --------------------------------------------------------------- */


/**
 * Settings renders the preferences page. Layout:
 *   - Left column: profile card with avatar and account info
 *   - Right column: AI preferences (tone slider, auto-draft toggle,
 *     vocabulary chips) and security settings (2FA)
 *
 * Will be connected to GET /settings, PATCH /settings/ai, and
 * DELETE /settings/data in Phase 11.
 *
 * @returns {JSX.Element} the settings page
 */
function Settings() {
  return (
    <div className="max-w-6xl mx-auto">
      {/* Page header */}
      <div className="mb-8">
        <h2 className="text-[32px] font-bold leading-[1.2] tracking-[-0.02em] text-on-surface mb-2">
          Settings
        </h2>
        <p className="text-[15px] text-on-surface-variant">
          Manage your AI preferences, security, and account details.
        </p>
      </div>

      {/* Tabs navigation */}
      <div className="flex items-center gap-6 border-b border-surface-container-high mb-8 pb-2">
        <button className="text-[12px] font-semibold tracking-[0.05em] text-primary border-b-2 border-primary pb-2">
          Account Profile
        </button>
        <button className="text-[12px] font-semibold tracking-[0.05em] text-on-surface-variant hover:text-primary transition-colors pb-2">
          AI Preferences
        </button>
        <button className="text-[12px] font-semibold tracking-[0.05em] text-on-surface-variant hover:text-primary transition-colors pb-2">
          Notifications
        </button>
        <button className="text-[12px] font-semibold tracking-[0.05em] text-on-surface-variant hover:text-primary transition-colors pb-2">
          Security
        </button>
      </div>

      {/* Content grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-[1.5rem]">
        {/* Left column: Profile card */}
        <div className="lg:col-span-4 flex flex-col gap-[1.5rem]">
          <div className="bg-surface-container-lowest rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-surface-bright p-[1.25rem] relative overflow-hidden">
            {/* Gradient header */}
            <div className="absolute top-0 left-0 w-full h-24 bg-gradient-to-r from-primary/10 to-secondary/10"></div>
            <div className="relative z-10 flex flex-col items-center mt-6">
              {/* Avatar placeholder */}
              <div className="w-24 h-24 rounded-full border-4 border-surface-container-lowest shadow-sm bg-surface-container-high flex items-center justify-center">
                <span className="text-[32px] font-semibold text-on-surface-variant">AI</span>
              </div>
              <h3 className="text-[20px] font-semibold mt-4">AI Assistant</h3>
              <p className="text-[13px] text-on-surface-variant">Pro Account</p>

              {/* Account details */}
              <div className="w-full mt-6 space-y-4">
                <div className="flex justify-between items-center py-2 border-b border-surface-container-low">
                  <span className="text-[13px] text-on-surface-variant">Email</span>
                  <span className="text-[13px] font-medium">user@example.com</span>
                </div>
                <div className="flex justify-between items-center py-2 border-b border-surface-container-low">
                  <span className="text-[13px] text-on-surface-variant">Role</span>
                  <span className="text-[13px] font-medium">Administrator</span>
                </div>
                <div className="flex justify-between items-center py-2">
                  <span className="text-[13px] text-on-surface-variant">Timezone</span>
                  <span className="text-[13px] font-medium">UTC -05:00</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Right column: AI Preferences + Security */}
        <div className="lg:col-span-8 flex flex-col gap-[1.5rem]">
          {/* AI Preferences card */}
          <div className="bg-surface-container-lowest rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-surface-bright p-[1.25rem]">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-[20px] font-semibold">AI Preferences</h3>
              <span className="bg-primary/10 text-primary text-[12px] font-semibold tracking-[0.05em] px-3 py-1 rounded-full">
                Active
              </span>
            </div>
            <p className="text-[14px] text-on-surface-variant">
              AI preference controls will be implemented in Phase 11.
            </p>
          </div>

          {/* Security card */}
          <div className="bg-surface-container-lowest rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-surface-bright p-[1.25rem] flex items-center justify-between">
            <div>
              <h3 className="text-[15px] font-medium flex items-center gap-2">
                <span className="material-symbols-outlined text-secondary">security</span>
                Two-Factor Authentication
              </h3>
              <p className="text-[13px] text-on-surface-variant mt-1">
                Add an extra layer of security to your account.
              </p>
            </div>
            <button className="px-4 py-2 bg-surface-container-lowest border border-outline-variant text-on-surface text-[12px] font-semibold tracking-[0.05em] rounded-lg hover:bg-surface-container-low transition-colors shadow-sm">
              Enable
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Settings;
