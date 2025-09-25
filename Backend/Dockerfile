# Final Corrected Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and the entire Frontend subfolder
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]