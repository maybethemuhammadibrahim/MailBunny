/* TodoCard.jsx
 * ---------------------------------------------------------------
 * Renders a single to-do item as a card with checkbox, title,
 * due date, and priority badge. Clicking the checkbox marks
 * the todo as done via the API. Phase 7 will implement fully.
 * --------------------------------------------------------------- */


/**
 * TodoCard displays a single task item extracted from an email.
 * Placeholder — will receive props (title, dueDate, priority,
 * source, isDone, onToggle) in Phase 7.
 *
 * @returns {JSX.Element} a task card component
 */
function TodoCard() {
  return (
    <div className="flex items-start gap-3 cursor-pointer group">
      <p className="text-[14px] text-on-surface-variant">
        TodoCard placeholder — Phase 7
      </p>
    </div>
  );
}

export default TodoCard;
