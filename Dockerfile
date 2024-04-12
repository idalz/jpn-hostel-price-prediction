FROM python:3.8-slim-buster

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE $PORT

# Command to run the application
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
