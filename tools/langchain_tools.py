# tools/langchain_tools.py
from langchain.agents import Tool
from tools.stock_tools import get_stock_info, get_recent_trends
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun

tools = [
    Tool.from_function(
        func=get_stock_info,
        name="GetStockInfo",
        model = "gemma2-9b-it",  # specify model if needed
        description="Get stock profile info like PE ratio, sector, etc. Input: stock ticker (e.g., AAPL).",
    ),
    Tool.from_function(
        func=get_recent_trends,
        name="GetStockTrends",
        model = "gemma2-9b-it",  # specify model if needed  
        description="Analyze recent trend from last 5 days' closing prices. Input: stock ticker."
    ),
    Tool.from_function(
        func=DuckDuckGoSearchRun().run,
        name="SearchNews",
        model = "gemma2-9b-it",  # specify model if needed
        description="Search for latest stock news. Input: stock ticker."
    )
]


# # Tools
# tools = [
#     Tool(name="GetStockInfo", func=get_stock_info, description="Get basic metrics of a stock."),
#     Tool(name="GetStockTrends", func=get_recent_trends, description="Get 5-day trend of a stock."),
#     Tool(name="SearchNews", func=DuckDuckGoSearchRun().run, description="Search for latest stock news."),
# ]
