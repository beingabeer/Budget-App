# pull official base image
FROM python:3.8.0-alpine
LABEL ABEER SEWAK

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# install pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

# copy project
COPY . /usr/src/app/


RUN adduser -D abeer
USER abeer


# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]





