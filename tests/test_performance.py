import time
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_efficiency_average_response_time():
    test_text = {"text": "UI가 정말 예쁘고 깔끔해서 앱을 쓸 때마다 기분이 너무 좋아요!"}
    
    total_time = 0
    iterations = 10
    
    # Warm-up (Load model completely before test to exclude initial loading time)
    client.post("/analyze", json=test_text)
    
    for _ in range(iterations):
        start_time = time.time()
        response = client.post("/analyze", json=test_text)
        end_time = time.time()
        
        assert response.status_code == 200
        total_time += (end_time - start_time)
        
    avg_time = total_time / iterations
    print(f"Average response time over {iterations} iterations: {avg_time:.4f} seconds")
    
    # Efficiency requirement: average response time < 1.5 seconds
    assert avg_time < 1.5, f"Test failed! Average response time {avg_time:.4f}s exceeded 1.5s limit."
