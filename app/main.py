from fastapi import FastAPI
from app.graph.workflow import workflow

app = FastAPI(title="Prometheus X")


@app.get("/")
def home():
    return {"message": "Prometheus X is running 🚀"}


@app.get("/research")
def research(topic: str):
    return workflow.invoke({
        "topic": topic,
        "plan": "",
        "report": ""
    })