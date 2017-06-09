import scrapy, os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.tatacliq_spider1 import MySpider1
from spiders.tatacliq_spider2 import MySpider2
from spiders.tatacliq_spider3 import MySpider3
from spiders.tatacliq_spider4 import MySpider4
from spiders.tatacliq_spider5 import MySpider5
from spiders.tatacliq_spider6 import MySpider6
from spiders.tatacliq_spider7 import MySpider7
from spiders.tatacliq_spider8 import MySpider8
from spiders.tatacliq_spider9 import MySpider9
from spiders.tatacliq_spider10 import MySpider10
from spiders.tatacliq_spider11 import MySpider11
from spiders.tatacliq_spider12 import MySpider12

log_file = '/'.join(os.path.abspath('').split('/')[:-3]) + '/logs/tatacliq.log'
if os.path.exists(log_file):
    os.remove(log_file)

process = CrawlerProcess(get_project_settings())
process.crawl(MySpider1)
process.crawl(MySpider2)
process.crawl(MySpider3)
process.crawl(MySpider4)
process.crawl(MySpider5)
process.crawl(MySpider6)
process.crawl(MySpider7)
process.crawl(MySpider8)
process.crawl(MySpider9)
process.crawl(MySpider10)
process.crawl(MySpider11)
process.crawl(MySpider12)
process.start()

