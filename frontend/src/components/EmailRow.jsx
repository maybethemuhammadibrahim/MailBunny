/* EmailRow.jsx
 * ---------------------------------------------------------------
 * Renders a single email row in the inbox list. Shows sender
 * avatar initials, sender name, subject, AI summary preview,
 * timestamp, and priority badge. Phase 8 will implement fully.
 * --------------------------------------------------------------- */


/**
 * EmailRow displays a single email in the inbox list pane.
 * Placeholder — will receive props (sender, subject, summary,
 * timestamp, priorityScore, isActive, onClick) in Phase 8.
 *
 * @returns {JSX.Element} an inbox email row component
 */
function EmailRow() {
  return (
    <div className="flex flex-col gap-1 p-4 hover:bg-surface-bright cursor-pointer transition-colors">
      <p className="text-[14px] text-on-surface-variant">
        EmailRow placeholder — Phase 8
      </p>
    </div>
  );
}

export default EmailRow;
