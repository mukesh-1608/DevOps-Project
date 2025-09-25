# backend/Dockerfile

# 1. Start with an official Python base image. We use 'slim' for a smaller size.
FROM python:3.9-slim

# 2. Set the working directory inside the container to /app.
WORKDIR /app

# 3. Copy the list of dependencies into the container.
COPY ./requirements.txt .

# 4. Install the dependencies. --no-cache-dir keeps the image smaller.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our application's code into the container.
COPY . .

# 6. Tell Docker that our application listens on port 5000.
EXPOSE 5000

# 7. Specify the command to run when the container starts. This starts our web server.
CMD ["python", "app.py"]