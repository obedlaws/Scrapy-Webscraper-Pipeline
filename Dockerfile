# MAIN SCRAPY APP

FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3-pip

RUN pip install Scrapy
RUN pip install psycopg2-binary

WORKDIR /scrapy-app

COPY itScrape ./

CMD [ "scrapy", "crawl", "books"]
