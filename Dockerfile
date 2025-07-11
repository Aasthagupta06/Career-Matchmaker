# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/
RUN python manage.py collectstatic --noinput
# Collect static files (will be used later)
# RUN python manage.py collectstatic --noinput

# Default command to run the Django app (we'll update this for migrations later)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
