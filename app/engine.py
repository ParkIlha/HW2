from transformers import pipeline

MODEL_NAME = "matthewburke/korean_sentiment"

class NLPEngine:
    def __init__(self):
        # Initialize pipeline. Load model.
        self.classifier = pipeline("sentiment-analysis", model=MODEL_NAME)
        
    def analyze_sentiment(self, text: str):
        result = self.classifier(text)[0]
        label = result["label"]
        score = result["score"]
        
        # matthewburke/korean_sentiment outputs LABEL_1 (긍정) or LABEL_0 (부정)
        if "1" in label or "POSITIVE" in label.upper() or "긍정" in label:
            emotion = "긍정적이에요 🤩"
        elif "0" in label or "NEGATIVE" in label.upper() or "부정" in label:
            emotion = "부정적이에요 😭"
        else:
            emotion = "보통이에요 😐"
            
        return {
            "label": emotion,
            "score": score
        }

# Singleton instance
nlp_engine = NLPEngine()
