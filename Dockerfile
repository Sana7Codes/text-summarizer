FROM python:3.8-slim-bullseye

# Install necessary system dependencies
RUN apt-get update -y && \
    apt-get install -y awscli git && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Optional: expose port if using FastAPI or Flask
EXPOSE 8080

# Start the app
CMD ["python3", "app.py"]


