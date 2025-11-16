import React from "react";
import UploadForm from "./components/UploadForm";
import Summary from "./components/Summary";
import ChartView from "./components/ChartView";
import History from "./components/History";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Chemical Equipment Parameter Visualizer</h1>

      <UploadForm />

      <hr />

      <Summary />

      <ChartView />

      <History />
    </div>
  );
}

export default App;
