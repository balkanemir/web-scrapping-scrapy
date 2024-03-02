FROM python:3.12.2-bullseye

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /jobs_project/jobs_project

CMD ["scrapy", "crawl", "json_spider"]
