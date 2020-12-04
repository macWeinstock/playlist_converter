FROM python:3.7
MAINTAINER Mac Weinstock "mac.weinstock@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["server.py"]