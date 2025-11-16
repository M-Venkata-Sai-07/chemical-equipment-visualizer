import React, { useEffect, useState } from "react";
import API from "../services/api";

function Summary() {
  const [summary, setSummary] = useState(null);

  const loadData = async () => {
    const res = await API.get("/history/");
    if (res.data.length > 0) {
      setSummary(res.data[0].summary);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  if (!summary) return <p>No summary available yet.</p>;

  return (
    <div>
      <h3>Summary</h3>
      <p>Total Records: {summary.total_records}</p>
      <p>Average Flowrate: {summary.avg_flowrate}</p>
      <p>Average Pressure: {summary.avg_pressure}</p>
      <p>Average Temperature: {summary.avg_temperature}</p>
    </div>
  );
}

export default Summary;
