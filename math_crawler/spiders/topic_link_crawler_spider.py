
import scrapy
from scrapy.selector import Selector
from math_crawler.items import TopicLinkItem
class TopicLinkCrawlerSpider(scrapy.Spider):
    name = 'topic_link_spider'

    allowed_domains = ["tech12h.com"]
    start_urls = [
        "https://tech12h.com/cong-nghe/cac-dang-toan-lop-5.html",
    ]

    def parse(self, response):
        topic_links = Selector(response).xpath('//div[@class="list-view block-content-body my_set"]/div')
        list_link = []
        for topic_link in topic_links:
            x = TopicLinkItem()
            x["topic_link"] = topic_link.xpath(
                'a/@href').extract()
            x["topic_title"] = topic_link.xpath(
                'a/@title').extract()
            yield x

