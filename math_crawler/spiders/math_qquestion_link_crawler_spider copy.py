
import scrapy
from scrapy.selector import Selector
from math_crawler.items import TopicLinkItem
import json

class TopicLinkCrawlerSpider(scrapy.Spider):
    name = 'math_qa_link_spider'
    allowed_domains = ["tech12h.com"]

    with open("topic_link_math5.json", 'r', encoding='utf-8') as file:
        topic_links_json = json.load(file)
    topic_links = [topic_link["topic_link"][0] for topic_link in topic_links_json]
    topic_links = ["https://tech12h.com/" + link for link in topic_links]
    start_urls = topic_links

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
    
    def parse(self, response):
        topic_links = Selector(response).xpath('//span[@class="field-content a_xanh"]')
        for topic_link in topic_links:
            x = TopicLinkItem()
            x["math_question_link"] = topic_link.xpath(
                'a/@href').extract()

            yield x

