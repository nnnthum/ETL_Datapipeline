# Use Python latest (Slim Image)
FROM python:3.9-slim

WORKDIR /app

# Copy dependencies and Install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY to Container
COPY . .

# python3 is default
CMD ["python3", "main.py"]
