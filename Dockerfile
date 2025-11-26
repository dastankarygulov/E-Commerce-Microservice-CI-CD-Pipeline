# Use a lightweight official Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Command to run the application using gunicorn for production stability
# The -w parameter specifies the number of worker processes (e.g., 2 workers)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
