# -*- coding: utf-8 -*-
import scrapy


class hunSpider(scrapy.Spider):
    name = "hunSpider"
    start_urls = [
        'https://www.brainyquote.com/authors/nicole-scherzinger-quotes',
    ]

    def parse(self, response):
        for lists in response.xpath('//*[@class="qll-bg"]'):

            #   //*[@id="qpos_1_1"]
            #   //*[@id="qpos_1_2"]/div/div[1]/div/a/text()

            #   //*[@id="qpos_1_1"]/div/div[1]/div/div/a

            #   //*[@id="qpos_1_1"]/div/div[3]/div/a[@class="oncl_list_kc"]
            yield {
                # 'text': lists.xpath('.//div/div[1]/div/a/text()').extract_first(),
                'text': lists.xpath('.//div[@class="clearfix"]/a/text()').extract_first(),
                'author': lists.xpath('.//div[@class="clearfix"]/div/a/text()').extract_first(),
                'tags': lists.xpath('.//div[@class="kw-box"]/a/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

