from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from ai_stock_agent import ask_stock_question
from main import get_financial_expert_analysis

app = FastAPI()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StockRequest(BaseModel):
    query: str

@app.post("/api/analyze-stock")
async def analyze_stock(request: StockRequest):
    try:
        # Get the analysis from your existing code
        analysis = get_stock_analysis(request.query)
        
        # Convert to JSON-serializable format
        response = {
            "basic_analysis": analysis["basic"],
            "expert_analysis": analysis["expert"]
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Modify your main.py to return a dict
def get_stock_analysis(query: str):
    response = ask_stock_question(query)
    expert_analysis = get_financial_expert_analysis(response['output'])
    
    return {
        "basic": response['output'],
        "expert": expert_analysis
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)