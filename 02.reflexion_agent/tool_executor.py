from dotenv import load_dotenv
import os

load_dotenv()

from langchain_core.tools import StructuredTool
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

from schemas import AnswerQuestion, ReviseAnswer


tavily_tool = None

try:
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if tavily_api_key:
        tavily_tool = TavilySearch(max_results=5, tavily_api_key=tavily_api_key)
    else:
        tavily_tool = TavilySearch(max_results=5)
except Exception as exc:
    tavily_tool = None
    print("[WARNING] Tavily tool not initialized. Set TAVILY_API_KEY to enable external search.", exc)


def run_queries(search_queries: list[str], **kwargs):
    """Run the generated queries."""
    if tavily_tool is None:
        # Fallback behavior for local execution without external Tavily key
        return [{"query": query, "result": "fake result: no TAVILY_API_KEY"} for query in search_queries]
    return tavily_tool.batch([{"query": query} for query in search_queries])


execute_tools = ToolNode(
    [
        StructuredTool.from_function(run_queries, name=AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name=ReviseAnswer.__name__),
    ]
)