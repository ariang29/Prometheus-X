from app.services.ai_service import ask_gemini


class ReportAgent:

    def generate(self, report: str, citations: str):

        prompt = f"""
Convert the following research into a professional report.

Requirements:
- Executive Summary
- Detailed Sections
- Bullet Points
- Markdown formatting
- Conclusion

Append this References section exactly at the end.

References

{citations}

Research

{report}
"""

        return ask_gemini(prompt)