# Backend/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else from the Backend folder (including the Frontend sub-folder)
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]