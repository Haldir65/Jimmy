# -*- coding: utf-8 -*-

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.spiders import Spider
from fictions.items import  DoubanMovieItem
# 在python3.5 virtual 环境下 run ，不要在乎不识别
# scrapy crawl douban_movie_top250 -o douban.csv
# https://zhuanlan.zhihu.com/p/24769534

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }


    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')

        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item
