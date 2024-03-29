# Use Python's official Docker image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /code/

# Expose the port that Django runs on
EXPOSE 8000

# Define the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
