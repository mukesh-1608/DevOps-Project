# Backend/Dockerfile

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application Python file
COPY app.py .

# Copy your local "Frontend" folder into a new folder called "static" inside the container
COPY Frontend/ /app/static/

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]