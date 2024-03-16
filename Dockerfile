# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3.12 -

# Install dependencies using poetry
RUN /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install --no-dev --no-interaction --no-ansi

# Change to the src directory
WORKDIR /app/src

# Expose the port that FastAPI will run on
EXPOSE 8000

# Railway pass env to image with the following args
ARG DB_PVZ
ARG PVZ_ENV
ARG PORT

# Command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]