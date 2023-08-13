# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for PostgreSQL
ENV POSTGRES_DB onlinejudge
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 1234
ENV POSTGRES_HOST localhost
ENV POSTGRES_PORT 5432

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE myproject.settings
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Expose the port on which Django will run
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
