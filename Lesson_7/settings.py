BOT_NAME = 'leroy_scraper'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'Lesson_7.pipelines.LeroyDataScraperPipeline': 300,
    'Lesson_7.pipelines.LeroyImagesScraperPipeline': 150,
}

IMAGES_STORE = 'images'

LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'