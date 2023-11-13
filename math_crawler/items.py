# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MathCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    #h1_link = scrapy.Field() #link dang bai tong quat
    # = scrapy.Field() #link chi tiet cau hoi,dap an tung bai

class TopicLinkItem(scrapy.Item):
    topic_link = scrapy.Field()
    topic_title = scrapy.Field()

class LinkItem(scrapy.Item):
    math_question_link = scrapy.Field()
