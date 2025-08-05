from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.routes import feedback

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel Feedback Summarizer API")
app.include_router(feedback.router)
