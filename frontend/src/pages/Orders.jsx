/* Orders.jsx
 * ---------------------------------------------------------------
 * Order and purchase tracking page. Shows spending overview
 * stats at the top and a grid of order cards below. Phase 10
 * will implement the full functionality with live data.
 * --------------------------------------------------------------- */


/**
 * Orders renders the purchase tracking page. Layout:
 *   - Top: spending overview cards (total spending, active deliveries, monthly avg)
 *   - Bottom: grid of order cards with status badges and tracking buttons
 *
 * Will be connected to GET /orders and GET /orders/stats in Phase 10.
 *
 * @returns {JSX.Element} the orders tracking page
 */
function Orders() {
  return (
    <div className="flex flex-col gap-[1.5rem] max-w-7xl mx-auto">
      {/* Spending overview section */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-[1.5rem]">
        {/* Primary spending card */}
        <div className="md:col-span-2 bg-surface-container-lowest rounded-xl p-[1.25rem] shadow-[0px_4px_20px_rgba(0,0,0,0.03)] border border-surface-container flex flex-col justify-between">
          <div>
            <h2 className="text-[14px] text-on-surface-variant mb-2">
              Total Spending This Year
            </h2>
            <div className="text-[32px] font-semibold leading-[1.2] tracking-[-0.02em] text-on-surface">
              $0.00
            </div>
          </div>
          {/* Chart placeholder */}
          <div className="mt-8 flex items-end gap-2 h-24 w-full">
            <div className="w-full bg-surface-container-highest rounded-t-sm h-[30%]"></div>
            <div className="w-full bg-surface-container-highest rounded-t-sm h-[50%]"></div>
            <div className="w-full bg-surface-container-highest rounded-t-sm h-[40%]"></div>
            <div className="w-full bg-surface-container-highest rounded-t-sm h-[60%]"></div>
            <div className="w-full bg-surface-container-highest rounded-t-sm h-[70%]"></div>
          </div>
        </div>

        {/* Secondary stat cards */}
        <div className="flex flex-col gap-[1.5rem]">
          <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] shadow-[0px_4px_20px_rgba(0,0,0,0.03)] border border-surface-container flex-1 flex flex-col justify-center">
            <div className="flex items-center gap-3 mb-2">
              <div className="p-2 rounded-lg bg-surface-container-low text-primary">
                <span className="material-symbols-outlined text-[20px]">local_shipping</span>
              </div>
              <h3 className="text-[14px] text-on-surface-variant">Active Deliveries</h3>
            </div>
            <div className="text-[20px] font-semibold text-on-surface">0 Orders</div>
          </div>
          <div className="bg-surface-container-lowest rounded-xl p-[1.25rem] shadow-[0px_4px_20px_rgba(0,0,0,0.03)] border border-surface-container flex-1 flex flex-col justify-center">
            <div className="flex items-center gap-3 mb-2">
              <div className="p-2 rounded-lg bg-surface-container-low text-primary">
                <span className="material-symbols-outlined text-[20px]">receipt_long</span>
              </div>
              <h3 className="text-[14px] text-on-surface-variant">Monthly Average</h3>
            </div>
            <div className="text-[20px] font-semibold text-on-surface">$0.00</div>
          </div>
        </div>
      </section>

      {/* Recent orders section */}
      <section className="flex flex-col gap-6 mt-4">
        <h2 className="text-[20px] font-semibold text-on-surface">Recent Orders</h2>
        <p className="text-[14px] text-on-surface-variant">
          Order tracking data will appear here once order emails are processed (Phase 10).
        </p>
      </section>
    </div>
  );
}

export default Orders;
