import React, { useState } from "react";

function App() {
  const [data, setData] = useState([]);

  const upload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8010/reconcile", {
      method: "POST",
      body: formData
    });

    const result = await res.json();
    setData(result);
  };

  return (
    <div>
      <h1>Finance AI</h1>

      <input type="file" onChange={upload} />

      <table border="1">
        <thead>
          <tr>
            {data[0] &&
              Object.keys(data[0]).map((key) => <th key={key}>{key}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              {Object.values(row).map((val, j) => (
                <td key={j}>{val}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
