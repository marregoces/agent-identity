# Demo service for the Agent Identity Explorer's github-agent.
FROM python:3.12.7-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
