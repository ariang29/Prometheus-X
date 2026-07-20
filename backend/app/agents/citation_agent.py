class CitationAgent:
    def generate(self, sources):
        citations = []

        for i, source in enumerate(sources, start=1):
            title = source.get("title", "Untitled")
            url = source.get("url", "")
            citations.append(f"[{i}] {title} - {url}")

        return "\n".join(citations)