FROM python:latest

ENV PYTHONUNBUFFERED=1
COPY requirements.txt /temp/requirements.txt

COPY frontier /frontier
WORKDIR /frontier
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password frontier-user

USER frontier-user
