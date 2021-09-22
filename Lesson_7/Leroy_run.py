from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from Lesson_7 import settings
from Lesson_7.spiders.Leroy import LeroyScraperSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroyScraperSpider)
    process.start()