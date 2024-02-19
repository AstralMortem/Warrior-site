FROM python

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False


RUN pip install --upgrade pip
COPY ../../backend/. /app/
RUN pip install -r requirements.txt
