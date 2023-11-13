# import scrapy
# from scrapy_selenium import SeleniumRequest
# from scrapy.selector import Selector
# from crawler.items import CrawlerItem

# class MathCrawlerSpider(scrapy.Spider):
#     name = 'math_spider'

#     def start_requests(self):
#         yield SeleniumRequest(url='http://example.com', callback=self.parse)

#     def parse(self, response):
#         # Extract data from the dynamic content
#         # ...

