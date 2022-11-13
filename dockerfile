FROM python:3.8-slim-buster

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y \
net-tools dnsutils \
curl procps htop

COPY ./app /app
WORKDIR /app

CMD [ "python3", "main.py"]