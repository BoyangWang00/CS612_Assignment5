FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python3
COPY httpserver.py /
COPY data.txt /
CMD python3 httpserver.py