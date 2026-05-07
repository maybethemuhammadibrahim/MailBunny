/* AnalyticsChart.jsx
 * ---------------------------------------------------------------
 * Renders email analytics charts using Recharts. Includes a
 * donut chart for email categories, a bar chart for sender
 * domains, and a security summary card. Phase 7 will implement
 * the full charts with live data.
 * --------------------------------------------------------------- */


/**
 * AnalyticsChart displays email analytics visualisations.
 * Placeholder — will use Recharts (PieChart, BarChart) with
 * data from GET /analytics/overview and GET /analytics/security
 * in Phase 7.
 *
 * @returns {JSX.Element} the analytics chart component
 */
function AnalyticsChart() {
  return (
    <div className="flex flex-col md:flex-row items-center justify-around gap-[1.5rem] mt-4">
      <p className="text-[14px] text-on-surface-variant">
        AnalyticsChart placeholder — Phase 7 (uses Recharts)
      </p>
    </div>
  );
}

export default AnalyticsChart;
