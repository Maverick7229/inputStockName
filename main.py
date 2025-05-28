# # main.py
# from ai_stock_agent import ask_stock_question
# from ticker_agent import analyze_stock_with_ticker_agent
# import os

# # query = "Give me detailed insights about jio stock including trend and metrics"
# query = "Give me detailed insights about bajaj finance stock including trend and metrics"

# # response = analyze_stock_with_ticker_agent(query)
# response = ask_stock_question(query)
# print(response)

# main.py
from ai_stock_agent import ask_stock_question
from ticker_agent import analyze_stock_with_ticker_agent
from langchain.prompts import PromptTemplate
from llm_groq import llm
from langchain.chains import LLMChain
import os

# Financial Expert Analysis Function
def get_financial_expert_analysis(stock_info):
    expert_prompt = PromptTemplate(
        input_variables=["stock_info"],
        template="""
        You are a senior financial analyst with 20 years of experience in equity research. 
        Provide professional investment advice based on the following stock information:
        
        {stock_info}
        
        Your analysis should include:
        1. All the relevant financial metrics and trends
        2. A detailed valuation assessment (overvalued/undervalued/fairly valued) with justification
        3. Technical analysis of the trend
        4. Fundamental analysis of the financial metrics
        5. Risk assessment
        6. Clear buy/hold/sell recommendation with price targets
        7. Long-term prospects analysis

        Present your analysis in professional format with clear sections.

        """
    )
    
    # llm = ChatOpenAI(temperature=0, model="gpt-4")
    expert_chain = LLMChain(llm=llm, prompt=expert_prompt)
    return expert_chain.run(stock_info=stock_info)

# Main execution
query = "Give me detailed insights about bajaj finance stock including trend and metrics"
response = ask_stock_question(query)

print("\n=== BASIC STOCK ANALYSIS ===")
print(response['output'])

print("\n=== FINANCIAL EXPERT ANALYSIS ===")
expert_analysis = get_financial_expert_analysis(response['output'])
print(expert_analysis)