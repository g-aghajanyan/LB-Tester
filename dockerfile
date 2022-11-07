FROM python:3.8-slim-buster

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8080
CMD [ "python3", "main.py"]