# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsProjectItem(scrapy.Item):
    slug = scrapy.Field()
    language = scrapy.Field()
    req_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    location_name = scrapy.Field()
    street_address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    country_code = scrapy.Field()
    postal_code = scrapy.Field()
    update_date = scrapy.Field()
    create_date = scrapy.Field()
