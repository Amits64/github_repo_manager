# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install requests 

# Copy the rest of the application code into the container
COPY . .

# Set environment variables (if needed)
ENV PYTHONPATH=/app

# Run the application
CMD ["python3", "github_repo_manager/main.py"]

