# -*- coding: utf-8 -*-
import scrapy


class hunSpider(scrapy.Spider):
    name = "hunSpider"
    start_urls = [
        'https://www.brainyquote.com/authors/nicole-scherzinger-quotes',
    ]

    def parse(self, response):
        for lists in response.xpath('//*[@class="qll-bg"]'):
            yield {
                'text': lists.xpath('.//div[@class="clearfix"]/a/text()').extract_first(),
                'author': lists.xpath('.//div[@class="clearfix"]/div/a/text()').extract_first(),
                'tags': lists.xpath('.//div[@class="kw-box"]/a/text()').extract()
            }