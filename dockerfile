FROM python:3.10.4-slim

WORKDIR /backend

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONIOENCODING=UTF-8
ENV SHELL=/bin/sh LANG=en_US.UTF-8

RUN apt-get update && \
  apt-get install -y \
  wget \
  net-tools \
  build-essential \
  libpq-dev \
  python3-dev

COPY requirements.txt /backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend/
CMD gunicorn