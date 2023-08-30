import scrapy


class SpeakerspiderSpider(scrapy.Spider):
    name = "speakerspider"
    allowed_domains = ["jbl.com"]
    start_urls = ["https://jbl.com/bluetooth-speakers/"]

    def parse(self, response):
        products = response.css('div.tile-body')
        for product in products:
            item = {
            'name' : product.css('a::text').get(),
            'price' : product.css('span.value::text').get()
            }
            yield item

        pass
