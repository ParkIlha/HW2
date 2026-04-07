from transformers import pipeline

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"

class NLPEngine:
    def __init__(self):
        # Initialize pipeline. Load model.
        self.classifier = pipeline("sentiment-analysis", model=MODEL_NAME)
        
    def analyze_sentiment(self, text: str):
        result = self.classifier(text)[0]
        label = result["label"]
        score = result["score"]
        
        # Map stars (1-5) to Korean sentiment
        try:
            stars = int(label.split()[0])
        except:
            stars = 3
            
        if stars >= 4:
            emotion = "긍정적이에요 🤩"
        elif stars == 3:
            emotion = "보통이에요 😐"
        else:
            emotion = "부정적이에요 😭"
            
        return {
            "label": emotion,
            "score": score
        }

# Singleton instance
nlp_engine = NLPEngine()
