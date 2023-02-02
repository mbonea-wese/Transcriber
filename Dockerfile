FROM python:3.8.16

WORKDIR /usr/src/nginx
COPY . .
RUN apt-get update
RUN apt install -y ffmpeg
RUN python3 -m pip install -r requirements.txt 
CMD uvicorn main:app --host 0.0.0.0 & celery worker --app=worker.celery --loglevel=info
EXPOSE 8000