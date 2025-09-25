# Backend/Dockerfile

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application file
COPY app.py .

# Copy the entire Frontend folder into a folder named 'static' inside the container
# This is the key fix that makes the files available to Flask
COPY Frontend/ /app/static/

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]