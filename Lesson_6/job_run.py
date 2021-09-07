"""I вариант
1) Доработать паука в имеющемся проекте, чтобы он формировал item по структуре:
*Наименование вакансии
*Зарплата от
*Зарплата до
*Ссылку на саму вакансию

*Сайт откуда собрана вакансия
И складывал все записи в БД(любую)

2) Создать в имеющемся проекте второго паука по сбору вакансий с сайта superjob.
Паук должен формировать item'ы по аналогичной структуре и складывать данные также в БД"""

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from Lesson_6 import settings
from Lesson_6.spiders.Job import JobScraperSpider


crawler_settings = Settings()
crawler_settings.setmodule(settings)
process = CrawlerProcess(settings=crawler_settings)
process.crawl(JobScraperSpider)
process.start()
