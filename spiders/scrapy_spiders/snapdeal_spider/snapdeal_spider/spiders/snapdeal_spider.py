import scrapy, sys
sys.path.append('/home/john/Scripts/upwork_projects/scraping/functions')
from functions import csv_opener
from snapdeal_functions import snapdeal_item_parser

class MySpider(scrapy.Spider):
    name = 'snapdeal'
    start_urls = ['https://www.snapdeal.com']

    fh = csv_opener('snapdeal')

    def parse(self, response):
        urls = [
            'https://www.snapdeal.com/product/jbl-t100a-in-ear-earphone/1808955798#bcrumbLabelId:288',
            'https://www.snapdeal.com/product/lyf-flame-8gb-black-grey/678753796085',
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        snapdeal_item_parser(response, self.fh)