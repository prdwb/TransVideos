import scrapy
from VideoCrawler.items import VideocrawlerItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class VideoCrawler(scrapy.Spider):
    name = 'VideoCrawler'
    allowed_domains = ['youtube.com']
    start_urls = [
        'https://www.youtube.com/user/djbendine/videos',
        'https://www.youtube.com/channel/UCVYamHliCI9rw1tHR1xbkfw/videos',
        'https://www.youtube.com/user/LauraVitalesKitchen/videos',
        'https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q/videos'
    ]

    def parse(self, response):
        for href in response.xpath('//li[@class="channels-content-item yt-shelf-grid-item"]/div/div/div/span/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parseVideoInfo)

    def parseVideoInfo(self, response):
        item = VideocrawlerItem()
        item['title'] = response.xpath('//span[@class="watch-title"]/@title').extract()
        item['url'] = response.url
        item['author'] = response.xpath('//div[@class="yt-user-info"]/a/text()').extract()
        item['description'] = response.xpath('//p[@id="eow-description"]/text()').extract()[0]
        item['upload_date'] = response.xpath('//strong[@class="watch-time-text"]/text()').extract()
        yield item
