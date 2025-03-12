# LangChain Groq AI Agent

## Overview
This project implements an AI-powered agent using **LangChain** and **Groq AI**, capable of performing web searches, generating text-based responses, and retrieving real-time data. The agent leverages **SerpAPI** for fetching real-time information and interacts dynamically using the **Zero-Shot ReAct** agent model.

## Features
- **AI-driven conversations** using **Groq AI**.
- **Real-time web search** with **SerpAPI**.
- **Dynamic query handling** via LangChain's agent framework.
- **Prebuilt use cases** including news updates, jokes, and stock price retrieval.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- API keys for **Groq AI** and **SerpAPI**

### Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/langchain-groq-agent.git
   cd langchain-groq-agent
   ```
2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Set your API keys** in `main.py`:
   ```python
   GROQ_API_KEY = "your_groq_api_key"
   SERP_API_KEY = "your_serpapi_key"
   ```
4. **Run the script**:
   ```sh
   python main.py
   ```

## Usage

The AI agent can handle various queries, such as:
- "What's the latest news on AI?"
- "Tell me a joke."
- "What's the time now in India?"

## Project Structure
```
├── main.py             # Main script to run the agent
├── requirements.txt    # Required dependencies
├── README.md           # Project documentation
```

## License
This project is licensed under the **MIT License**.

## Contributing
Feel free to contribute by submitting issues or pull requests. Let's enhance this AI agent together! 🚀

