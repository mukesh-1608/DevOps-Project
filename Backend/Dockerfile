# backend/Dockerfile

# Start with an official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (it's in the same folder)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (from the current folder)
COPY . .

# Tell Docker that our application listens on port 5000
EXPOSE 5000

# Specify the command to run when the container starts
CMD ["python", "app.py"]