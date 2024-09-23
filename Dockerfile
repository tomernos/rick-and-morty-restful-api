FROM python:3.9-slim

RUN apt-get update -y && apt-get install curl wget -y

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=RestAPI.py

CMD ["flask", "run", "--host=0.0.0.0"]: