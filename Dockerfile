# syntax=docker/dockerfile:1

FROM python:3.10.6-alpine3.16
RUN apk add git build-base linux-headers libffi-dev
WORKDIR /sample_app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

