# syntex=docker/dockerfile:1

#FROM python:3.8-slim-buster

#WORKDIR /app-docker

#COPY req.txt req.txt
#RUN pip3 install -r req.txt

#COPY . . 

#CMD ["python3","-m","flask","run","--host=0.0.0.0"]



FROM python
WORKDIR /attendanceApp
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY req.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r req.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
