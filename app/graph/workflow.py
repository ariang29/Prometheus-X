from typing import TypedDict

from langgraph.graph import StateGraph

from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent


class AgentState(TypedDict):
    topic: str
    plan: str
    report: str


planner = PlannerAgent()
researcher = ResearchAgent()


def planner_node(state: AgentState):
    plan = planner.plan(state["topic"])
    return {
        **state,
        "plan": plan
    }


def research_node(state: AgentState):
    report = researcher.research(state["topic"])
    return {
        **state,
        "report": report
    }


graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("research", research_node)

graph.add_edge("planner", "research")

graph.set_entry_point("planner")
graph.set_finish_point("research")

workflow = graph.compile()