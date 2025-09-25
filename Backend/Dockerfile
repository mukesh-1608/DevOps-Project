# Final, Corrected Dockerfile

FROM python:3.9-slim

# The working directory inside the container
WORKDIR /app

# Copy the requirements file from the build context (the Backend folder)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python application file
COPY app.py .

# Copy the Frontend sub-folder into a new folder called 'static' inside the container
COPY Frontend/ /app/static/

# Expose the port
EXPOSE 5000

# The command to run the application
CMD ["python", "app.py"]