import React, { useState } from "react";

import { AgGridReact } from "ag-grid-react";

import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

function App() {

  const [data, setData] = useState([]);

  const upload = async (e) => {

    const file = e.target.files[0];

    const formData = new FormData();

    formData.append("file", file);

    const res = await fetch(
      "http://localhost:8010/reconcile",
      {
        method: "POST",
        body: formData
      }
    );

    const result = await res.json();

    setData(result);
  };

  const columnDefs = data[0]
    ? Object.keys(data[0]).map((key) => ({
        field: key
      }))
    : [];

  return (

    <div style={{ padding: 20 }}>

      <h1>Finance AI</h1>

      <input
        type="file"
        onChange={upload}
      />

      <div
        className="ag-theme-alpine"
        style={{
          height: 500,
          marginTop: 20
        }}
      >

        <AgGridReact
          rowData={data}
          columnDefs={columnDefs}
        />

      </div>

    </div>
  );
}

export default App;
