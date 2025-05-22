# Use a slim official Python image
FROM python:3.10-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Set working directory (empty — code will be bind-mounted here)
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Install Python packages from requirements.txt (assumes it's part of the image)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Run streamlit, expecting app.py to be provided at runtime via mount
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
