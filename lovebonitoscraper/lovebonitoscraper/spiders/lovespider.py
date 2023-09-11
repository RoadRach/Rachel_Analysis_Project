import scrapy


class LovespiderSpider(scrapy.Spider):
    name = "lovespider"
    allowed_domains = ["www.lovebonito.com"]
    start_urls = ["https://www.lovebonito.com/sg/shop/apparel-accessories/dresses?stock.is_in_stock=true"]

    def parse(self, response):
        product = response.css('div.sf-product-card')
        for p in product:
            yield{'name' : p.css('h3.sf-product-card__title::text').get().replace('\n',''),
                  'price' : p.css('div.sf-product-card__price::text').get().replace('\n','')
            }
