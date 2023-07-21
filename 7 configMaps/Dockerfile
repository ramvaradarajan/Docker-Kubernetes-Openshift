# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the application
ENV CONFIG_VALUE=default_value

# Run the Python application
CMD [ "python", "app.py" ]
