# Using the official Python 3.8 image as a our base image
FROM python:3.8

# Setting our working directory inside the Docker container to /app
WORKDIR /app

COPY . .

CMD ["python", "./bakery.py"]