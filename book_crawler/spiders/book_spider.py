# -*- coding: utf-8 -*-
import scrapy, json, datetime
from book_crawler.settings import MAX_SITES_TO_SCRAPE


class BookSpider(scrapy.Spider):

    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/category/books_1/index.html']

    scraped_urls = set()

    def parse(self, response):

        with open('statistics.txt', 'a') as file:
            stats = self.crawler.stats.get_stats()
            timediff = datetime.datetime.utcnow() - stats['start_time']
            output = '{} {} {} {} {}\n'.format(
                timediff.seconds,
                stats['scheduler/enqueued/memory'],
                stats['downloader/response_count'],
                stats['downloader/request_bytes'],
                stats.get('dupefilter/filtered', 0)
            )
            file.write(output)

        #ensure first time being scraped
        if response.url not in BookSpider.scraped_urls:
            BookSpider.scraped_urls.add(response.url)

            #determine if book page
            if 'index.html' in response.url and 'category/books' not in response.url:

                #extract book data
                category = response.css('li a').re('.*/category/books/.*>(.*)</a>')[0].encode('utf-8')
                title = response.xpath('//li[4]/text()')[0].extract().encode('utf-8')
                description = response.xpath('//p[1]/text()')[1].extract().strip('...more').encode('utf-8')

                #write each page of data to a file
                if category != 'Add a comment':
                    filename = 'data/{}.txt'.format(category.replace(' ', '_'))
                    with open(filename, 'a') as file:
                        file.write(json.dumps({title:description}, ensure_ascii=False))

            #follow new links from page
            for a in response.css('li a'):
                if self.crawler.stats.get_value('item_scraped_count') < MAX_SITES_TO_SCRAPE:
                    yield response.follow(a, callback=self.parse)