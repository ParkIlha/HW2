document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const chatHistory = document.getElementById('chatHistory');
    const sendBtn = document.getElementById('sendBtn');

    // 스크롤 맨 아래로 이동
    const scrollToBottom = () => {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    };

    // 메시지 UI 추가 함수
    const appendMessage = (sender, text, score = null, raw_emotion = null, advice = null) => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}`;
        if (raw_emotion) {
            msgDiv.classList.add(`emotion-${raw_emotion}`);
        }
        
        let content = text;
        if (score !== null && sender === 'bot') {
            content += `<span class="score-text">정확도: ${(score * 100).toFixed(1)}%</span>`;
        }

        msgDiv.innerHTML = `<div class="bubble">${content}</div>`;
        chatHistory.appendChild(msgDiv);
        scrollToBottom();
        
        // 조언(Advice)이 있을 경우 두 번째 위로/조언 말풍선을 띄움
        if (advice) {
            setTimeout(() => {
                const adviceDiv = document.createElement('div');
                adviceDiv.className = `message ${sender}`;
                adviceDiv.innerHTML = `<div class="bubble" style="background:#fff; color:#333; box-shadow:0 4px 10px rgba(0,0,0,0.05); border:1px solid #eee;">💡 ${advice}</div>`;
                chatHistory.appendChild(adviceDiv);
                scrollToBottom();
            }, 600); // 0.6초 딜레이
        }
    };

    // 로딩 말풍선 추가 함수
    const addTypingIndicator = () => {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot';
        typingDiv.id = 'typingIndicator';
        typingDiv.innerHTML = `<div class="bubble typing"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>`;
        chatHistory.appendChild(typingDiv);
        scrollToBottom();
    };

    // 로딩 말풍선 제거 함수
    const removeTypingIndicator = () => {
        const indicator = document.getElementById('typingIndicator');
        if (indicator) {
            indicator.remove();
        }
    };

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = userInput.value.trim();
        if (!text) return;

        // 1. 사용자 메시지 화면에 표시
        appendMessage('user', text);
        userInput.value = '';
        sendBtn.disabled = true;

        // 2. 타이핑 인디케이터 표시
        addTypingIndicator();

        try {
            // 3. API 요청 전송
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error('API 요청에 실패했습니다.');
            }

            const data = await response.json();
            
            // 4. 로딩 제거 및 봇 메시지 표시
            removeTypingIndicator();
            appendMessage('bot', data.label, data.score, data.raw_emotion, data.advice);

        } catch (error) {
            removeTypingIndicator();
            appendMessage('bot', '죄송합니다. 네트워크 오류가 발생했습니다. 😔');
            console.error(error);
        } finally {
            sendBtn.disabled = false;
            userInput.focus();
        }
    });
});
