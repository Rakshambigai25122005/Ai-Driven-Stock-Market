import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function App() {
  const [ticker, setTicker] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [prediction, setPrediction] = useState(null);

  const fetchPrediction = async () => {
    const response = await fetch("http://localhost:5000/api/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ticker, startDate, endDate }),
    });

    const data = await response.json();
    setPrediction(data);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <Card className="max-w-xl mx-auto p-6 shadow-xl rounded-2xl bg-white">
        <CardContent>
          <h1 className="text-2xl font-bold mb-4 text-center">
            Cracking the Market Code
          </h1>
          <p className="text-gray-500 text-center mb-6">
            AI-Driven Stock Prediction with Time Series Analysis
          </p>

          <input
            type="text"
            placeholder="Enter Stock Ticker (e.g. AAPL)"
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
            className="w-full mb-4 p-2 border rounded-md"
          />
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            className="w-full mb-4 p-2 border rounded-md"
          />
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            className="w-full mb-4 p-2 border rounded-md"
          />
          <Button className="w-full" onClick={fetchPrediction}>
            Predict
          </Button>

          {prediction && (
            <div className="mt-6 bg-gray-50 p-4 rounded-md">
              <h2 className="text-xl font-semibold mb-2">Prediction Result</h2>
              <pre className="text-sm text-gray-700">
                {JSON.stringify(prediction, null, 2)}
              </pre>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
