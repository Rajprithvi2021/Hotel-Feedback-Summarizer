from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Header, HTTPException

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(x_api_key: str = Header(default=None)):
    from app.core.config import OPENAI_API_KEY
    if x_api_key != OPENAI_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")