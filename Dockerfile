# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the Hugging Face model during build step
# This caches the model in the docker image so it doesn't download on startup
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')"

# Copy project files
COPY app/ /workspace/app/
COPY tests/ /workspace/tests/

# Expose port
EXPOSE 8000

# Start server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
