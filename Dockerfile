# /Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy backend requirements and install
COPY Backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY Backend/app.py .

# Copy the entire Frontend folder into a 'static' directory in the image
COPY Frontend/ /app/static/

EXPOSE 5000

CMD ["python", "app.py"]