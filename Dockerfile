FROM python:3.7.3-alpine

LABEL Name=polestar Version=0.0.1
EXPOSE 8000

WORKDIR /app
ADD . /app

# Install common dependencies (psycopg2)
RUN apk add --no-cache postgresql-dev

RUN apk update \
    && apk add --no-cache --virtual .build-deps build-base linux-headers gcc musl-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del .build-deps
