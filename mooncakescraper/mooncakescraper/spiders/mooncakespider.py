import scrapy


class MooncakespiderSpider(scrapy.Spider):
    name = "mooncakespider"
    allowed_domains = ["https://sg.iherb.com"]
    start_urls = ["https://sg.iherb.com/c/vitamin-c"]

    def parse(self, response):
        product = response.css('.product-inner')
        for p in product:
            yield{'name' : p.css('.absolute-link-wrapper > div:nth-of-type(2)::attr(content)').extract(),
                  'price' : "price"
            }

    # name = "lovespider"
    # allowed_domains = ["www.lovebonito.com"]
    # start_urls = ["https://www.lovebonito.com/sg/shop/apparel-accessories/dresses?stock.is_in_stock=true"]

    # def parse(self, response):
    #     product = response.css('div.sf-product-card')
    #     for p in product:
    #         yield{'name' : p.css('h3.sf-product-card__title::text').get().replace('\n',''),
    #               'price' : p.css('div.sf-product-card__price::text').get().replace('\n','')
    #         }