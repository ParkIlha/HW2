from fastapi import FastAPI
from pydantic import BaseModel
from app.engine import nlp_engine

app = FastAPI(title="NLP Sentiment Analysis API")

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

@app.get("/")
def read_root():
    return {"message": "NLP API Server is running."}

@app.post("/analyze", response_model=SentimentResponse)
def analyze(request: TextRequest):
    result = nlp_engine.analyze_sentiment(request.text)
    return result
