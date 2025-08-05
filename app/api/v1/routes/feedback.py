from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.dependencies import get_db
from app.schemas.feedback import FeedbackIn, FeedbackOut, ThemedFeedbackResponse, FeedbackStats
from app.db.models import Feedback
from app.db.database import SessionLocal
from app.services.summarizer import group_comments_by_theme, summarize_themes, get_feedback_stats

router = APIRouter()


@router.post("/feedback", response_model=FeedbackOut)
def add_feedback(feedback: FeedbackIn, db: Session = Depends(get_db)):
    fb = Feedback(guest_id=feedback.guest_id, comment=feedback.comment)
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb

@router.get("/feedback/themes", response_model=ThemedFeedbackResponse)
def get_theme_summaries(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).all()
    theme_map = group_comments_by_theme(feedbacks)
    summaries = summarize_themes(theme_map)
    return {"themes": summaries}

@router.get("/feedback/stats", response_model=FeedbackStats)
def get_stats(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).all()
    return get_feedback_stats(feedbacks)
