# Use official Python image
FROM python:3.13-slim

# Install system dependencies for mysqlclient and pillow
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start server
CMD ["gunicorn", "projectportfolio.wsgi:application", "--bind", "0.0.0.0:8000"]

# Build the Docker image with the tag 'myportfolio'
# docker build -t myportfolio .
