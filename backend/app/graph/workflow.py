from typing import TypedDict
from langgraph.graph import StateGraph

from app.agents.planner_agent import PlannerAgent
from app.agents.web_search_agent import WebSearchAgent
from app.agents.research_agent import ResearchAgent
from app.agents.citation_agent import CitationAgent
from app.agents.report_agent import ReportAgent


class AgentState(TypedDict):
    topic: str
    plan: str
    web_results: list
    report: str
    citations: str


planner = PlannerAgent()
web_search = WebSearchAgent()
researcher = ResearchAgent()
citation = CitationAgent()
report_agent = ReportAgent()


def planner_node(state: AgentState):
    return {
        **state,
        "plan": planner.plan(state["topic"])
    }


def web_search_node(state: AgentState):
    return {
        **state,
        "web_results": web_search.search(state["topic"])
    }


def research_node(state: AgentState):
    return {
        **state,
        "report": researcher.research(
            state["topic"],
            state["web_results"]
        )
    }


def citation_node(state: AgentState):
    return {
        **state,
        "citations": citation.generate(
            state["web_results"]
        )
    }


def report_node(state: AgentState):
    return {
        **state,
        "report": report_agent.generate(
            state["report"],
            state["citations"]
        )
    }


graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("web_search", web_search_node)
graph.add_node("research", research_node)
graph.add_node("citation", citation_node)
graph.add_node("report", report_node)

graph.add_edge("planner", "web_search")
graph.add_edge("web_search", "research")
graph.add_edge("research", "citation")
graph.add_edge("citation", "report")

graph.set_entry_point("planner")
graph.set_finish_point("report")

workflow = graph.compile()