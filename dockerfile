FROM python:3.11-slim

# Create non-root user — required for OpenShift SCC
RUN groupadd -r flaskops && useradd -r -g flaskops flaskops

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

USER flaskops
EXPOSE 8080
CMD ["python", "main.py"]
