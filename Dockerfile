FROM python:3.10-slim-bullseye

# Install necessary system dependencies
RUN apt-get update -y && \
    apt-get install -y --fix-missing \
        awscli \
        git \
        build-essential \
        libxml2-dev \
        libxslt-dev \
        zlib1g-dev \
        libffi-dev \
        pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies  
RUN pip install --no-cache-dir --upgrade pip
# Install packages individually to avoid hash conflicts
RUN pip install --no-cache-dir --timeout=300 --retries=3 \
    transformers[sentencepiece] \
    datasets \
    sacrebleu \
    rouge_score \
    py7zr \
    pandas \
    nltk \
    tqdm \
    PyYAML \
    matplotlib \
    torch \
    beartype \
    python-box
RUN pip install --no-cache-dir -e .

# Expose port for using FastAPI 
EXPOSE 8080

# Start the app
CMD ["python3", "src/app.py"]

