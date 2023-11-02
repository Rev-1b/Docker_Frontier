FROM python:latest


COPY requirements.txt /temp/requirements.txt

COPY frontier /frontier
WORKDIR /frontier
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password frontier-user

USER frontier-user
