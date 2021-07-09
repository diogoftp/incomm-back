FROM python:3.8-alpine
RUN apk update && apk upgrade && apk add --update alpine-sdk && apk add build-base && apk add libffi-dev && apk add --update py-pip && apk add --no-cache tzdata
ENV TZ America/Sao_Paulo
ADD ./requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && python -m pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5002
CMD python ./scripts/database_generator.py
CMD python ./server.py
