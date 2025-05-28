#extpert_chain.py
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm_groq import llm

def get_financial_expert_chain():
    prompt = PromptTemplate(
        input_variables=["stock_info", "trend_info", "news_info"],
        template="""
You are a financial analyst. Based on the following data:
- Stock Metrics: {stock_info}
- Stock Price Trend: {trend_info}
- Recent News Headlines: {news_info}

Provide:
1. An expert analysis of the stock's current position.
2. A prediction of the likely short-term trend (upward/downward/stagnant).
3. Justification for your prediction using metrics + news.
4. Suggested action (buy/hold/sell) with reasoning.

Answer like a seasoned financial advisor.
"""
    )
    # llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")  # or llama3-70b
    return LLMChain(llm=llm, prompt=prompt)
