from collections import defaultdict, Counter
from app.core.config import OPENAI_API_KEY
from app.core.prompts import theme_summarization_prompt
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

THEME_LIST = ["Cleanliness", "Staff & Service", "Food & Dining", "Location", "Amenities"]
KEYWORDS = {
    "clean": "Cleanliness",
    "staff": "Staff & Service",
    "service": "Staff & Service",
    "food": "Food & Dining",
    "dining": "Food & Dining",
    "location": "Location",
    "amenities": "Amenities"
}


def classify_by_keywords(comment: str) -> list[str]:
    comment_lower = comment.lower()
    return [theme for keyword, theme in KEYWORDS.items() if keyword in comment_lower]


def classify_with_llm(comment: str) -> list[str]:
    prompt = f"""
You are a classifier for hotel guest feedback.

Classify the following comment into one or more of these themes:
- Cleanliness
- Staff & Service
- Food & Dining
- Location
- Amenities

Only return a comma-separated list of matching themes (no explanation).

Comment: "{comment}"
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        content = response.choices[0].message.content
        return [t.strip() for t in content.split(",") if t.strip() in THEME_LIST]
    except Exception as e:
        print("⚠️  LLM classification failed. Falling back to keyword method.")
        return classify_by_keywords(comment)


def group_comments_by_theme(feedbacks: list) -> dict:
    theme_map = defaultdict(list)
    for fb in feedbacks:
        themes = classify_with_llm(fb.comment)
        for theme in themes:
            theme_map[theme].append(fb.comment)
    return theme_map

def summarize_themes(theme_map: dict) -> list[dict]:
    summaries = []
    for theme, comments in theme_map.items():
        prompt = theme_summarization_prompt(theme, comments)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response.choices[0].message.content.strip()
        summaries.append({"name": theme, "summary": summary})
    return summaries


def get_feedback_stats(feedbacks: list) -> dict:
    theme_counts = Counter()
    negative_themes = Counter()

    for fb in feedbacks:
        themes = classify_with_llm(fb.comment)
        for theme in themes:
            theme_counts[theme] += 1
            if "not" in fb.comment.lower() or "bad" in fb.comment.lower():
                negative_themes[theme] += 1

    total = len(feedbacks)
    most_common = theme_counts.most_common(1)[0][0] if theme_counts else None
    negative_ratio = {
        k: round(v / theme_counts[k], 2)
        for k, v in negative_themes.items()
        if theme_counts[k] > 0
    }

    return {
        "total_feedback": total,
        "most_common_theme": most_common,
        "negative_theme_ratio": negative_ratio
    }
