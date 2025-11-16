import React, { useState } from "react";
import API from "../services/api";

function UploadForm() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const uploadFile = async () => {
    if (!file) {
      alert("Please choose a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const res = await API.post("/upload/", formData);
    setMessage("Upload Success!");
    console.log(res.data);
  };

  return (
    <div>
      <h3>Upload CSV File</h3>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} /><br/><br/>
      <button onClick={uploadFile}>Upload</button>
      <p>{message}</p>
    </div>
  );
}

export default UploadForm;
