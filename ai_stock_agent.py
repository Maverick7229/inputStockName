# ai_stock_agent.py
from langchain.agents import initialize_agent
from llm_groq import llm
from tools.langchain_tools import tools

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    # agent="conversational-react-description",
    verbose=True
)

def ask_stock_question(question: str):
    return agent.invoke({"input": question})






# from langchain.agents import initialize_agent, Tool
# from langchain.agents.agent_types import AgentType
# from tools.stock_tools import get_stock_info, get_recent_trends
# from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
# from expert_chain import get_financial_expert_chain  # if in separate file
# from llm_groq import llm



# # Tools
# tools = [
#     Tool(name="GetStockInfo", func=get_stock_info, description="Get basic metrics of a stock."),
#     Tool(name="GetStockTrends", func=get_recent_trends, description="Get 5-day trend of a stock."),
#     Tool(name="SearchNews", func=DuckDuckGoSearchRun().run, description="Search for latest stock news."),
# ]

# agent = initialize_agent(
#     tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
# )

# def ask_stock_question(query: str):
#     stock_info = get_stock_info(query.split()[-1])  # last word as symbol
#     trend_info = get_recent_trends(query.split()[-1])
#     news = DuckDuckGoSearchRun().run(f"{query} stock news")
#     expert_chain = get_financial_expert_chain()
#     advice = expert_chain.run({
#         "stock_info": stock_info,
#         "trend_info": trend_info,
#         "news_info": news
#     })
#     return advice
