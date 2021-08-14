from ubuntu:latest

RUN apt update
RUN apt -y install python python3-pip

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY main.py .
ENTRYPOINT python3 main.py
