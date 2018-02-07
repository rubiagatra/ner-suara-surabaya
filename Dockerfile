FROM python:3.6-slim-stretch

MAINTAINER Doni Rubiagatra <rubiagatra@gmail.com>

RUN apt-get update 
RUN apt-get -y install build-essential make gcc python3-dev 
RUN mkdir -p /ner-api
WORKDIR /ner-api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000  --access-logfile - wsgi:app


