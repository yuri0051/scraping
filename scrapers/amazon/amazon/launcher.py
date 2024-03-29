import scrapy, os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.amazon_scraper import MySpider

log_file = '/'.join(os.path.abspath('').split('/')[:-3]) + '/logs/amazon.log'
if os.path.exists(log_file):
    os.remove(log_file)

process = CrawlerProcess(get_project_settings())
process.crawl(MySpider)
process.start()

