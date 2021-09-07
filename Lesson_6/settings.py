BOT_NAME = 'Lesson_6'

SPIDER_MODULES = ['Lesson_6.spiders']
NEWSPIDER_MODULE = 'Lesson_6.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'Lesson_6.pipelines.JobScraperPipeline': 300,
}

LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
