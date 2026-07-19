from app.services.ai_service import ask_gemini
from app.prompts.research_prompt import RESEARCH_PROMPT

class ResearchAgent:

    def research(self, topic: str):
        prompt = RESEARCH_PROMPT.format(topic=topic)
        return ask_gemini(prompt)
    from app.logger import logger