# Base image with Python
FROM python:3.9

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
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Tell Docker which port Flask runs on
EXPOSE 7860

# Command to run the app
CMD ["python", "app.py"]