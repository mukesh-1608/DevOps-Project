# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# --- NEW: Copy the frontend files into a 'static' folder ---
COPY ./frontend/ /app/static/

# Copy the backend requirements file
COPY ./backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code
COPY ./backend/ .

EXPOSE 5000

CMD ["python", "app.py"]