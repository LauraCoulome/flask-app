# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src/app.py .

# Set an environment variable
ARG APP_ENV=development
ENV APP_ENV=${APP_ENV}

# Command to run the application
CMD ["python", "app.py"]

