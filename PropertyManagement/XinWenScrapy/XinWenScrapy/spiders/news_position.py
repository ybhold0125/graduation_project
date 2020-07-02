# -*- coding: utf-8 -*-
import scrapy

from XinWenScrapy.items import XinwenscrapyItem


class NewsPositionSpider(scrapy.Spider):
    name = 'news_position'
    allowed_domains = ['hgdaily.com.cn']
    start_urls = ['http://www.hgdaily.com.cn/w/3/ciye/4O18293O1.html']

    def parse(self, response):
        for ArticleList in response.xpath('//div[@class="ArticleList"]/ul/li'):
            item = XinwenscrapyItem()
            item['news_title'] = ArticleList.xpath('./a/strong/text()').extract_first()
            item['news_time'] = ArticleList.xpath('./span/font/text()').extract_first()
            item['news_summary'] = ArticleList.xpath('./samp/text()').extract_first()
            link = ArticleList.xpath('./a/@href').extract_first()
            yield scrapy.Request(
                'http://www.hgdaily.com.cn' + link,
                callback=self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        text = response.xpath('//div[@class="Web_Default_Content"]/p/text()').extract()
        item['news_detail'] = ''.join(text)
        yield item