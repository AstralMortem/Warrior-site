FROM python:latest

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ../../backend/. /src/
RUN pip install -r requirements.txt
