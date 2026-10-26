
# Start with a Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install pip dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY src/ ./src/

# Define a build argument
ARG APP_ENV=development

# Set environment variable using the build argument
ENV APP_ENV=$APP_ENV

# Run the application when the container starts
CMD ["python", "src/app.py"]

