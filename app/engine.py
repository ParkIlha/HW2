from transformers import pipeline

MODEL_NAME = "bhadresh-savani/bert-base-multilingual-cased-emotion"

class NLPEngine:
    def __init__(self):
        # Initialize pipeline. Load model.
        self.classifier = pipeline("text-classification", model=MODEL_NAME, top_k=1)
        
    def analyze_sentiment(self, text: str):
        result = self.classifier(text)[0]
        if isinstance(result, list): 
            result = result[0]
        
        label = result["label"].lower()
        score = result["score"]
        
        if label == "joy":
            emotion = "기뻐요! 😄"
        elif label == "sadness":
            emotion = "슬퍼요 😢"
        elif label == "anger":
            emotion = "화가 나요 😡"
        elif label == "fear":
            emotion = "조금 무서워요 😨"
        elif label == "love":
            emotion = "사랑스러워요 🥰"
        elif label == "surprise":
            emotion = "깜짝 놀랐어요! 😯"
        else:
            emotion = "보통이에요 😐"
            
        return {
            "label": emotion,
            "raw_emotion": label,
            "score": score
        }

# Singleton instance
nlp_engine = NLPEngine()
