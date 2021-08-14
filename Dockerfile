from ubuntu:latest

RUN apt update
RUN apt -y install python python3-pip

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 main.py