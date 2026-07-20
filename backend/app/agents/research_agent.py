from app.services.ai_service import ask_gemini


class ResearchAgent:

    def research(self, topic: str, web_results: list):

        context = ""

        for result in web_results:
            context += f"""
Title: {result.get('title')}
Content: {result.get('content')}
URL: {result.get('url')}

"""

        prompt = f"""
You are an expert research analyst.

Research Topic:
{topic}

Live Web Results:
{context}

Write a detailed, professional report using the information above.
Do not invent facts.
"""

        return ask_gemini(prompt)