# Prometheus-X

> **AI-powered research assistant built with FastAPI, LangGraph, Gemini, and Tavily.**

Prometheus-X is a learning project that explores how multiple AI agents can work together to turn a research topic into a structured report with web-based information and citations.

## ✨ What it does

- Accepts a research topic through a FastAPI endpoint
- Plans the research task with an AI agent
- Searches the web using Tavily
- Processes and synthesizes research using Gemini
- Generates citations for collected information
- Produces a final research report
- Stores completed research using SQLAlchemy

## 🧠 Architecture

```text
Research Topic
      ↓
 Planner Agent
      ↓
 Web Search Agent ──→ Tavily
      ↓
 Research Agent ────→ Gemini
      ↓
 Citation Agent
      ↓
 Report Agent
      ↓
 Structured Research Report
```

The workflow is orchestrated with **LangGraph**, connecting the individual agents into a research pipeline.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development language |
| FastAPI | Backend API |
| LangGraph | Multi-agent workflow orchestration |
| Google Gemini | AI research and generation |
| Tavily | Web search |
| SQLAlchemy | Database layer |
| Uvicorn | API server |

## 📁 Project Structure

```text
Prometheus-X/
├── app/
├── backend/
│   └── app/
│       ├── agents/
│       ├── graph/
│       ├── services/
│       └── main.py
├── frontend/
├── requirements.txt
└── README.md
```

## 🚀 Run locally

### 1. Clone the repository

```bash
git clone https://github.com/ariang29/Prometheus-X.git
cd Prometheus-X
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API keys

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 4. Start the backend

```bash
uvicorn backend.app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 🔎 Example API request

```text
GET /research?topic=artificial+intelligence
```

## 📚 Why I built this

I built Prometheus-X as a hands-on learning project to understand AI agents, workflow orchestration, APIs, web search, and how different AI components can be connected into one application.

The project also helped me learn how to structure a backend application and experiment with modern AI development tools.

## 📌 Project status

This is an ongoing learning project. I plan to continue improving the architecture, frontend experience, reliability, and research quality as I learn more.

## 👨‍💻 Author

**Arian Ghosh**

GitHub: https://github.com/ariang29

---

⭐ If you find the project interesting, feel free to explore the code and follow the project as it develops.
