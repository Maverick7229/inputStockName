# # ticker_agent.py
# from langchain.agents import initialize_agent, Tool
# from langchain.schema import BaseOutputParser
# from llm_groq import llm  # Your existing LLM
# import json
# import re
# from typing import Dict, Optional

# class TickerExtractionTool:
#     def __init__(self, json_path: str):
#         self.json_path = json_path
#         self.ticker_mapping = self._load_ticker_mapping()
    
#     def _load_ticker_mapping(self) -> Dict[str, str]:
#         try:
#             with open(self.json_path, 'r', encoding='utf-8') as file:
#                 return json.load(file)
#         except Exception as e:
#             print(f"Error loading ticker mapping: {e}")
#             return {}
    
#     def extract_ticker(self, query: str) -> str:
#         """Extract ticker symbol from query using the mapping."""
#         # Check if ticker already exists
#         ticker_pattern = r'\b[A-Z]{2,5}\.(?:BO|NS)\b'
#         existing_ticker = re.search(ticker_pattern, query)
#         if existing_ticker:
#             return f"Ticker found: {existing_ticker.group()}"
        
#         # Search for company names in the mapping
#         query_lower = query.lower()
#         for company_name, ticker in self.ticker_mapping.items():
#             company_words = company_name.lower().split()
#             if any(word in query_lower for word in company_words if len(word) > 2):
#                 return f"Ticker found: {ticker} for company: {company_name}"
        
#         return "No ticker symbol found in the mapping for this query."

# def create_ticker_agent(json_path: str):
#     """Create a LangChain agent for ticker extraction."""
#     ticker_tool = TickerExtractionTool(json_path)
    
#     tools = [
#         Tool(
#             name="ticker_extractor",
#             description="Extract stock ticker symbol from company names using BSE mapping",
#             func=ticker_tool.extract_ticker
#         )
#     ]
    
#     agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent="zero-shot-react-description",
#         verbose=True
#     )
    
#     return agent

# # Usage example for LangChain approach
# def analyze_stock_with_ticker_agent(query: str):
#     """Complete workflow using LangChain agent approach."""
#     ticker_agent = create_ticker_agent("D:\\agenticAI\\newStockAnalysis_git\\nse_ticker_mapping.json")
    
#     # First, extract ticker
#     ticker_response = ticker_agent.invoke({
#         "input": f"Extract the stock ticker symbol from this query: {query}"
#     })
    
#     print("Ticker extraction response:", ticker_response['output'])
    
#     # Then proceed with stock analysis
#     from ai_stock_agent import ask_stock_question
#     response = ask_stock_question(query)
#     return response

# ticker_agent.py
from langchain.agents import initialize_agent, Tool
from langchain.schema import BaseOutputParser
from llm_groq import llm  # Your existing LLM
import json
import re
from typing import Dict, Optional

class TickerExtractionTool:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.ticker_mapping = self._load_ticker_mapping()
    
    def _load_ticker_mapping(self) -> Dict[str, str]:
        try:
            with open(self.json_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading ticker mapping: {e}")
            return {}
    
    def extract_ticker(self, query: str) -> str:
        """Extract ticker symbol and company name from query using the mapping.""" 
        # Check if ticker already exists
        ticker_pattern = r'\b[A-Z]{2,5}\.(?:BO|NS)\b'
        existing_ticker = re.search(ticker_pattern, query)
        if existing_ticker:
            ticker_symbol = existing_ticker.group()
            # Find company name for this ticker
            for company_name, ticker_val in self.ticker_mapping.items():
                if ticker_val == ticker_symbol:
                    return f"Use ticker '{ticker_symbol}' for stock data and company name '{company_name}' for news search"
            return f"Use ticker '{ticker_symbol}' for all operations"
        
        # Search for company names in the mapping
        query_lower = query.lower()
        for company_name, ticker in self.ticker_mapping.items():
            company_words = company_name.lower().split()
            if any(word in query_lower for word in company_words if len(word) > 2):
                return f"Use ticker '{ticker}' for stock data and company name '{company_name}' for news search"
        
        return "No ticker symbol found in the mapping for this query."

def create_ticker_agent(json_path: str):
    """Create a LangChain agent for ticker extraction."""
    ticker_tool = TickerExtractionTool(json_path)
    
    tools = [
        Tool(
            name="ticker_extractor",
            description="Extract stock ticker symbol from company names using BSE mapping and return 2 things: 1--> full query replacing the <ticker> placeholder, 2--> ticker symbol for stock data",
            func=ticker_tool.extract_ticker
        )
    ]
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    
    return agent


def analyze_stock_with_ticker_agent(query: str):
    """Complete workflow using LangChain agent approach."""
    ticker_agent = create_ticker_agent("D:\\agenticAI\\newStockAnalysis_git\\bse_ticker_mapping.json")
    
    # First, extract ticker
    ticker_response = ticker_agent.invoke({
        "input": f"Extract the stock ticker symbol from this query: {query}"
    })
    print("Ticker raw extraction response:", ticker_response['output'])
    # if ticker_response is having "." in it then only use the ticker part before "."
    if '.' in ticker_response['output']:
        ticker_response['output'] = ticker_response['output'].split('.')[0]
    print("Ticker final extraction response:", ticker_response['output'])
    print(ticker_response)
    #  this is the ticker response "{'input': 'Extract the stock ticker symbol from this query: Give me detailed insights about vedanta stock including trend and metrics', 'output': 'VEDL'}", add the input and output to the query
    # query = f"Give me detailed insights about vedanta stock including trend and metrics. {ticker_response['output']}"
    # print("Final query for stock analysis:", query)
    
    # Then proceed with stock analysis
    from ai_stock_agent import ask_stock_question
    response = ask_stock_question(query)
    return response