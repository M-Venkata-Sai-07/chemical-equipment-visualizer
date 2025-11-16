import React, { useEffect, useState } from "react";
import API from "../services/api";

function History() {
  const [items, setItems] = useState([]);

  const loadHistory = async () => {
    const res = await API.get("/history/");
    setItems(res.data);
  };

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div>
      <h3>Upload History</h3>
      {items.length === 0 && <p>No history yet.</p>}
      <ul>
        {items.map((h) => (
          <li key={h.id}>{h.file_name}</li>
        ))}
      </ul>
    </div>
  );
}

export default History;
