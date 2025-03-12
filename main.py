import os
from langchain_groq import ChatGroq
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper

# Set API keys (Replace with your own keys)
GROQ_API_KEY = "your_groq_api_key"
SERP_API_KEY = "your_serpapi_key"

# Initialize LLM
llm = ChatGroq(api_key=GROQ_API_KEY)

# Initialize Search Tool
search = SerpAPIWrapper(serpapi_api_key=SERP_API_KEY)

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for fetching real-time information."
    )
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    # Example Queries
    queries = [
        "What's the latest news on AI?",
        "Tell me a joke",
        "What's the time now in India?",
        "What's the current stock price of Tata Steel?"
    ]

    for query in queries:
        response = agent.run(query)
        print(f"Query: {query}\nResponse: {response}\n")
