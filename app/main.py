import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.engine import nlp_engine

app = FastAPI(title="NLP Sentiment Analysis API")

# Mount static directory for CSS/JS
os.makedirs("app/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    raw_emotion: str
    score: float
    advice: str

@app.get("/")
def read_root():
    return FileResponse("app/static/index.html")

@app.post("/analyze", response_model=SentimentResponse)
def analyze(request: TextRequest):
    result = nlp_engine.analyze_sentiment(request.text)
    return result
