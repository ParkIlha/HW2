from transformers import pipeline

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

class NLPEngine:
    def __init__(self):
        # Initialize pipeline. Load model.
        self.classifier = pipeline("sentiment-analysis", model=MODEL_NAME)
        
    def analyze_sentiment(self, text: str):
        result = self.classifier(text)[0]
        return {
            "label": result["label"],
            "score": result["score"]
        }

# Singleton instance
nlp_engine = NLPEngine()
