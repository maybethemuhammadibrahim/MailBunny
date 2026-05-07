/* MeetingCard.jsx
 * ---------------------------------------------------------------
 * Renders a single meeting event card with title, date/time,
 * location or video link, and attendee initials. Phase 7 will
 * implement the full layout matching the mockup.
 * --------------------------------------------------------------- */


/**
 * MeetingCard displays a single meeting extracted from an email.
 * Placeholder — will receive props (title, date, time,
 * locationOrLink, attendees, source) in Phase 7.
 *
 * @returns {JSX.Element} a meeting card component
 */
function MeetingCard() {
  return (
    <div className="flex items-center gap-4 p-4 rounded-lg bg-surface-container-lowest border border-surface-variant">
      <p className="text-[14px] text-on-surface-variant">
        MeetingCard placeholder — Phase 7
      </p>
    </div>
  );
}

export default MeetingCard;
