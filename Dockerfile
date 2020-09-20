FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y
RUN apt install -y python3-pip firefox curl
RUN apt clean -y
RUN pip3 install selenium

RUN curl -Lo geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz
RUN tar xzf geckodriver.tar.gz
RUN mv geckodriver /usr/local/bin && rm geckodriver.tar.gz

ADD main.py /

ENTRYPOINT ["/usr/bin/python3", "/main.py"]