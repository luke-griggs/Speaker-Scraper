import scrapy


class SpeakerspiderSpider(scrapy.Spider):
    name = "speakerspider"
    allowed_domains = ["jbl.com"]
    start_urls = ["https://jbl.com/bluetooth-speakers/"]

    def parse(self, response):
        pass
