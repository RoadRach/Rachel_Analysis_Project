import scrapy


class MooncakespiderSpider(scrapy.Spider):
    name = "mooncakespider"
    allowed_domains = ["shopee.sg"]
    start_urls = ["https://shopee.sg"]

    def parse(self, response):
        pass
