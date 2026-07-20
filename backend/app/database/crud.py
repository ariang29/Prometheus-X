from sqlalchemy.orm import Session
from app.database.models import Research


def save_research(db: Session, topic: str, report: str):
    research = Research(
        topic=topic,
        report=report
    )
    db.add(research)
    db.commit()
    db.refresh(research)
    return research