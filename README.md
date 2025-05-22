# AI Applications

A Streamlit-based application for AI-related tasks.

## Setup

### Using Docker

1. Build the Docker image:
```bash
docker build -t ai-apps .
```

2. Run the container:
```bash
docker run -p 8501:8501 \
  -v $(pwd):/app \
  ai-apps
```

3. Open your browser and navigate to `http://localhost:8501`

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application file
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration for containerization

## Dependencies

- Streamlit: For interactive web interface
- OpenAI: For AI model integration
- Requests: For HTTP requests
- Pandas: For data manipulation

## License

MIT License
