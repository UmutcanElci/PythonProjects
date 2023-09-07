import scrapy


class QuotestrySpider(scrapy.Spider):
    name = "quotesTry"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        pass
