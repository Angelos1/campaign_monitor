# pull official base image
FROM python:3.8.1-alpine

# new
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd
    #&& \
    #apk add dos2unix

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# new
# add entrypoint.sh
#COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
#RUN chmod -R 777 /usr/src/app/entrypoint.sh
#RUN dos2unix /usr/src/app/entrypoint.sh
# add app
COPY . /usr/src/app

CMD python manage.py run -h 0.0.0.0