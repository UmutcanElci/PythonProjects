import scrapy
from ..items import QuotestoscrapeItem

class QuotestrySpider(scrapy.Spider):
    name = "quotesTry"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
    def parse(self, response):
        rows = response.xpath('//div')
        for row in rows:
            item = QuotestoscrapeItem()
            item['quote'] = row.xpath('.//span/text()').get()
            item['author'] = row.xpath('.//span/small/text()').get()
            yield item
        
