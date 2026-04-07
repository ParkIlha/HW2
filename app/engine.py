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
            advice = "저도 덩달아 기분이 좋아지네요! 긍정적인 에너지를 맘껏 즐기세요."
        elif label == "슬픔":
            emotion = "슬퍼요 😢"
            raw_emotion = "sadness"
            advice = "힘든 일이 있으셨군요. 따뜻한 차 한 잔 마시며 쉬어가는 건 어떨까요?"
        elif label == "분노":
            emotion = "화가 나요 😡"
            raw_emotion = "anger"
            advice = "화가 많이 나셨군요. 눈을 감고 심호흡을 크게 세 번 해보세요."
        elif label == "불안":
            emotion = "조금 불안해요 😨"
            raw_emotion = "fear"
            advice = "불안해하지 마세요. 당신은 안전합니다. 편안한 생각을 떠올려보세요."
        elif label == "당황":
            emotion = "깜짝 놀랐어요! 😯"
            raw_emotion = "surprise"
            advice = "깜짝 놀라셨군요! 잠시 멈춰서 상황을 차분하게 살펴보세요."
        else: # 평온
            emotion = "평온해요 😐"
            raw_emotion = "love" # map to calm styling
            advice = "마음이 편안하시네요. 오늘 이 여유로운 시간을 온전히 누리시길 바라요."
            
        return {
            "label": emotion,
            "raw_emotion": raw_emotion,
            "score": score,
            "advice": advice
        }

# Singleton instance
nlp_engine = NLPEngine()
