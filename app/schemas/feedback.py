from pydantic import BaseModel
from typing import List

class FeedbackIn(BaseModel):
    guest_id: str
    comment: str

class FeedbackOut(FeedbackIn):
    id: int

class ThemeSummary(BaseModel):
    name: str
    summary: str

class ThemedFeedbackResponse(BaseModel):
    themes: List[ThemeSummary]

class FeedbackStats(BaseModel):
    total_feedback: int
    most_common_theme: str
    negative_theme_ratio: dict
