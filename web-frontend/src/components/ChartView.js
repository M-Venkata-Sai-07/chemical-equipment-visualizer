import React, { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import API from "../services/api";
import { Chart as ChartJS } from "chart.js/auto";

function ChartView() {
  const [chartData, setChartData] = useState(null);

  const loadChart = async () => {
    const res = await API.get("/history/");
    if (res.data.length > 0) {
      const dist = res.data[0].summary.type_distribution;

      setChartData({
        labels: Object.keys(dist),
        datasets: [
          {
            label: "Equipment Type Count",
            data: Object.values(dist),
            backgroundColor: "rgba(75,192,192,0.6)"
          }
        ]
      });
    }
  };

  useEffect(() => {
    loadChart();
  }, []);

  if (!chartData) return <p>No chart data yet.</p>;

  return (
    <div>
      <h3>Type Distribution Chart</h3>
      <Bar data={chartData} />
    </div>
  );
}

export default ChartView;
