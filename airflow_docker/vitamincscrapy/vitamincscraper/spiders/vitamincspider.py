import scrapy


class VitamincspiderSpider(scrapy.Spider):
    name = "vitamincspider"
    allowed_domains = ["https://sg.iherb.com"]
    start_urls = ["https://sg.iherb.com/c/vitamin-c"]

    def parse(self, response):
        product = response.css('.product-inner')
        for p in product:
            yield{'name' : p.css('.absolute-link-wrapper > div:nth-of-type(2)::attr(content)').extract(),
                  'stars' : p.css('div:nth-of-type(2) > a:nth-of-type(2)::attr(title)').extract(),
                  'rating_no' : p.css('div:nth-of-type(2) > a:nth-of-type(2) > span::text').extract(),
                  'price' : p.css('div:nth-of-type(5) > .product-price-top > div > span > bdi::text').extract()
            }