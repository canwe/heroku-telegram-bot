FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN rm -rf aiotg/
RUN rm -rf .git/
RUN rm -rf .idea/

RUN apt-get update
RUN apt-get --assume-yes install mc

COPY requirements.txt ./
RUN pip install --no-cache-dir -Ur requirements.txt

RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

WORKDIR /usr/src/app/bot

ADD bot /usr/src/app/bot
ADD aiotg /usr/src/app/bot/aiotg

CMD ["python", "./main.py"]

EXPOSE 8080
