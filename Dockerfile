FROM python:latest

ENV PYTHONUNBUFFERED=1
COPY requirements.txt /temp/requirements.txt

COPY frontier /frontier
WORKDIR /frontier
EXPOSE 8000


#RUN apt-get update
#RUN apt-get install postgresql-client build-base postgresql-dev

RUN pip install --no-cache -r /temp/requirements.txt

RUN adduser --disabled-password frontier-user

USER frontier-user
