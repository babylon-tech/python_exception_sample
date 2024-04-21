FROM python:3.12.0-slim

WORKDIR /app

COPY src/ .

RUN apt-get update && apt-get install -y git
