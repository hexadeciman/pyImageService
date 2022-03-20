# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
EXPOSE 8080
WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD src/ .
ENV FLASK_APP=src/app.py                                                                                                       

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]