# 🏨 Hotel Feedback Summarizer API

This project is an **AI-powered API service** that collects hotel guest feedback, classifies it under relevant **themes** (like *Cleanliness*, *Food*, *Service*, etc.), generates concise **summaries** using an **LLM (OpenAI)**, and provides **statistics** on the feedback.

---

## 🚀 Features

- 🔄 Submit guest feedback via REST API
- 🧠 Automatically classify feedback into **hotel-related themes**
- ✨ Generate **LLM-powered summaries** per theme
- 📊 Provide **statistics** like common themes and negative feedback ratio
- 💾 Store feedback in **SQLite** using SQLAlchemy
- 🐳 Fully **Dockerized** for easy deployment
- ⚙️ Switch between **OpenAI** for summarization (fallback ready)

---

## 🧱 Tech Stack

- **Python 3.12**
- **FastAPI** (REST API)
- **SQLAlchemy + SQLite** (Database)
- **OpenAI** (LLM integration)
- **Docker & Docker Compose**

---

## 📁 Project Structure

```bash
hotel_feedback_api/
├── app/
│   ├── api/v1/routes/feedback.py       # API routes
│   ├── api/v1/dependencies.py          # DB dependencies
│   ├── core/config.py                  # API keys, settings
│   ├── core/prompts.py                 # Prompt templates
│   ├── db/database.py                  # DB session logic
│   ├── db/models.py                    # ORM models
│   ├── schemas/feedback.py             # Pydantic schemas
│   ├── services/summarizer.py          # LLM classification/summarization
│   └── main.py                         # App entrypoint
├── Dockerfile                          # Docker config
├── docker-compose.yml                  # Docker Compose config
├── .env                                # Environment variables
├── requirements.txt                    # Dependencies
└── README.md


## Setup Instructions

1. Clone the repository
    git clone https://github.com/your-username/hotel_feedback_api.git
    cd hotel_feedback_api

2. Create .env file
    OPENAI_API_KEY=sk-xxxxxx

3. Local Development (Without Docker)
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Run app
    uvicorn app.main:app --reload

4. Dockerized Setup
    # Build and run the container
    sudo docker-compose up --build


##API Endpoints

1. POST /feedback
    Submit a guest feedback.
    {
    "guest_id": "G001",
    "comment": "Room was clean, food arrived late and cold."
    }

2. GET /feedback/themes
    Returns summarized feedback for each detected theme (via OpenAI).

3. GET /feedback/stats
    Returns stats like:
        Total feedbacks
        Most common theme
        Negative feedback ratio by theme


##Supported Themes
Comments are grouped into these hotel-relevant themes:
    🧼 Cleanliness
    👥 Staff & Service
    🍽️ Food & Dining
    📍 Location
    🏢 Amenities

