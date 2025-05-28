import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('Give me detailed insights about bajaj finance stock');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeStock = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/analyze-stock', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });
      const data = await response.json();
      setAnalysis(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Stock Analysis Dashboard</h1>
        <div className="search-container">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter stock query"
          />
          <button onClick={analyzeStock} disabled={loading}>
            {loading ? 'Analyzing...' : 'Analyze Stock'}
          </button>
        </div>
        
        {analysis && (
          <div className="analysis-container">
            <div className="analysis-section">
              <h2>Basic Analysis</h2>
              <div className="analysis-content">
                <pre>{analysis.basic_analysis}</pre>
              </div>
            </div>
            
            <div className="analysis-section">
              <h2>Expert Analysis</h2>
              <div className="analysis-content">
                <pre>{analysis.expert_analysis}</pre>
              </div>
            </div>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;