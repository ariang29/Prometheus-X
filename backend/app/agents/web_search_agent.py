import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


class WebSearchAgent:
    def search(self, query: str):
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        return response.get("results", [])