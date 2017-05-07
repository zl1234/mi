#  -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from mi.items import ECommerceGoodItem
from mi.items import ECommerceGoodCommentItem
from mi.items import ECommerceShopCommentItem
from mi.items import ECommerceShopItem
import re
import requests
import json

class Spider_taobao(RedisCrawlSpider):

    name = 'taobao'
    redis_key = 'taobao:start_urls'
    allowed_domains = ['taobao.com']

    rules = {
        Rule(LinkExtractor(allow=('.*'), deny=()),callback='processGood',follow=True),
    }

    # 电商Id
    eCommerceId = 2

    # 获取商品信息
    def processGood(self,response):
        response.url
        url = response.url
        print url
        # 提取html
        #html = requests.get(url=url).content
        #print html