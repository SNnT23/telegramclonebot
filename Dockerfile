FROM python:latest
RUN apt update && apt upgrade -y
RUN apt install git pip curl python3-pip -y

WORKDIR /usr/src/app
COPY . .
RUN chmod 777 /usr/src/app

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt
RUN apt-get -qq purge git && apt-get -y autoremove && apt-get -y autoclean

CMD ["bash", "start.sh"]
