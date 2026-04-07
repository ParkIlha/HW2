from transformers import pipeline

MODEL_NAME = "Seonghaa/korean-emotion-classifier-roberta"

class NLPEngine:
    def __init__(self):
        # Initialize pipeline. Load model.
        self.classifier = pipeline("text-classification", model=MODEL_NAME)
        
    def analyze_sentiment(self, text: str):
        # By default, pipeline returns [{"label": "기쁨", "score": 0.99}]
        # Extract the first dict.
        result = self.classifier(text)[0]
        
        label = result["label"]
        score = result["score"]
        
        if label == "기쁨":
            emotion = "기뻐요! 😄"
            raw_emotion = "joy"
        elif label == "슬픔":
            emotion = "슬퍼요 😢"
            raw_emotion = "sadness"
        elif label == "분노":
            emotion = "화가 나요 😡"
            raw_emotion = "anger"
        elif label == "불안":
            emotion = "조금 불안/무서워요 😨"
            raw_emotion = "fear"
        elif label == "당황":
            emotion = "깜짝 놀랐어요! 😯"
            raw_emotion = "surprise"
        else: # 평온
            emotion = "평온해요 😐"
            raw_emotion = "love" # map to pink/calm
            
        return {
            "label": emotion,
            "raw_emotion": raw_emotion,
            "score": score
        }

# Singleton instance
nlp_engine = NLPEngine()
