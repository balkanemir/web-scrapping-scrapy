import json
import scrapy


class JobSpider(scrapy.Spider):
    name = "json_spider"
    custom_settings = {
        "ITEM_PIPELINES": {
            "jobs_project.pipelines.PostgresPipeline": 300,
        },
    }

    def __init__(self, **kwargs):
        name = "json_spider"

    def start_requests(self):
        json_files = [
            "file://./s01.json",
            "file://./s02.json",
        ]

        for json_file in json_files:
            yield scrapy.Request(
                url=json_file,
                callback=self.parse_page,
            )

    def parse_page(self, response):
        json_response = json.loads(response.body)

        if isinstance(json_response, dict) and "jobs" in json_response:
            jobs = json_response["jobs"]
            for job in jobs:
                data = job["data"]
                yield {
                    "slug": data.get("slug"),
                    "language": data.get("language"),
                    "req_id": data.get("req_id"),
                    "title": data.get("title"),
                    "description": data.get("description"),
                    "location_name": data.get("location_name"),
                    "street_address": data.get("street_address"),
                    "city": data.get("city"),
                    "state": data.get("state"),
                    "country": data.get("country"),
                    "country_code": data.get("country_code"),
                    "postal_code": data.get("postal_code"),
                    "update_date": data.get("update_date"),
                    "create_date": data.get("create_date"),
                }
