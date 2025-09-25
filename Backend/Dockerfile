# Final Corrected Dockerfile

FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main Python application file
COPY app.py .

# Copy your local "Frontend" folder into a new folder named "static" inside the container
# This is a key step that makes the web pages available to the server
COPY Frontend/ /app/static/

# Expose the port the application runs on
EXPOSE 5000

# The command to run the application
CMD ["python", "app.py"]