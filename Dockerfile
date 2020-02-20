FROM python:3.8.1-alpine3.10

RUN mkdir -p /opt/app/glad_glyphs
workdir /opt/app/glad_glyphs

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./glad_glyphs.py ./
COPY ./server.py ./
COPY ./templates/ ./templates
COPY ./static/ ./static

CMD gunicorn server:app