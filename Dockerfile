# Use a small Python base image
FROM python:3.9-slim-buster

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining files into container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]
