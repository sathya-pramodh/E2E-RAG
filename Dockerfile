# syntax=docker/dockerfile:1
FROM python:3.8-buster

WORKDIR /

COPY Makefile .
RUN make deps

COPY . .

EXPOSE 5000:5000

CMD [ "make", "deploy" ]
