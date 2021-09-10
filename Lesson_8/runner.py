from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Lesson_8.spiders.instagramparser import InstagramcomSpider
from Lesson_8 import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(InstagramcomSpider, users_list=['allegaeonofficial', 'digimortal_band'])
    process.start()

