# Using the official Python 3.8 image as the base image
FROM python:3.8

WORKDIR /app

COPY . .

CMD ["python", "./bakery.py"]