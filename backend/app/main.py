from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.graph.workflow import workflow
from app.database.database import engine, get_db
from app.database import models
from app.database.crud import save_research

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Prometheus X")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Prometheus X is running 🚀"}

@app.get("/research")
def research(topic: str, db: Session = Depends(get_db)):
    result = workflow.invoke({
        "topic": topic,
        "plan": "",
        "web_results": [],
        "report": "",
        "citations": ""
    })

    save_research(
        db=db,
        topic=topic,
        report=result["report"]
    )

    return result