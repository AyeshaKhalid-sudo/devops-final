FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . /app

EXPOSE 5001

# Make Flask listen on all interfaces
CMD ["python", "app.py"]

