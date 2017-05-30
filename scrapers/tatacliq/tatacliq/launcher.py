import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import logging
from scrapy.utils.log import configure_logging
from spiders.tatacliq_spider1 import MySpider1
from spiders.tatacliq_spider2 import MySpider2

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename = 'tatacliq.log',
    filemode = 'w',
    format = '%(levelname)s: %(message)s',
    level = logging.ERROR
)

process = CrawlerProcess(get_project_settings())
process.crawl(MySpider1)
process.crawl(MySpider2)
process.start()

