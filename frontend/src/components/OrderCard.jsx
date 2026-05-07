/* OrderCard.jsx
 * ---------------------------------------------------------------
 * Renders a single order/purchase card with product image,
 * retailer, item description, status badge, price, and tracking
 * button. Phase 10 will implement the full layout.
 * --------------------------------------------------------------- */


/**
 * OrderCard displays a single order extracted from an email.
 * Placeholder — will receive props (retailer, itemDescription,
 * status, price, trackingUrl, estimatedDelivery) in Phase 10.
 *
 * @returns {JSX.Element} an order card component
 */
function OrderCard() {
  return (
    <div className="bg-surface-container-lowest rounded-xl shadow-[0px_4px_20px_rgba(0,0,0,0.03)] border border-surface-container overflow-hidden">
      <p className="p-[1.25rem] text-[14px] text-on-surface-variant">
        OrderCard placeholder — Phase 10
      </p>
    </div>
  );
}

export default OrderCard;
