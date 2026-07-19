from app.services.ai_service import ask_gemini


class PlannerAgent:

    def plan(self, topic: str):
        prompt = f"""
You are an AI Project Planner.

Given the topic below, create a research plan.

Return only these sections:

1. Research Goals
2. Information Needed
3. Suggested Search Queries
4. Final Report Structure

Topic:
{topic}
"""
        return ask_gemini(prompt)