# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get -y update && \
    apt-get install binutils libproj-dev gdal-bin -y
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code/