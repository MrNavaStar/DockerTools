FROM debian:11-slim

RUN apt-get update
RUN apt-get install git
COPY . /app
WORKDIR /app
RUN git init -b master
RUN git remote add origin
RUN chmod +x update.sh

ENTRYPOINT ["cmd"]