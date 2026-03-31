# Base image with Python
FROM python:3.12-slim

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install flask ultralytics pillow opencv-python-headless

# Tell Docker which port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]