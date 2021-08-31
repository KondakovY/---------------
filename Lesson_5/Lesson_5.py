"""Написать программу, которая собирает «Новинки» с сайта техники mvideo и складывает данные в БД.
Сайт можно выбрать и свой. Главный критерий выбора: динамически загружаемые товары"""

from collections import defaultdict
from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

SHOP_PARAMS = [{'name': 'mvideo_new',
                'url': 'https://www.mvideo.ru/',
                'block': '//body/div[2]/div[1]/div[3]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]',
                'next': '/a[contains(@class, "right")]',
                'next_disabled': '/a[contains(@class, "right disabled")]',
                'products': '/div/ul/li//h3/a',
                'params_link': '//div[contains(@class, "o-pdp-about-product-specification__inner-block")]/a',
                'product_title': '//h1[@class="fl-h1"]',
                'product_price': '//div[@class="fl-pdp-price__current"]',
                'product_keys': '(//span[@class="product-details-overview-specification"])[position() mod 2 = 1]',
                'product_values': '(//span[@class="product-details-overview-specification"])[position() mod 2 = 0]'}]

              
def get_xpath(d: dict, key: str):
    """ Get value from dict, adding `block` """
    return d.get('block') + d.get(key)



chrome_options: Options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')
driver: WebDriver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
driver.implicitly_wait(3)

for shop in SHOP_PARAMS:
    driver.get(shop.get('url'))
    driver.execute_script("window.scrollTo(0, 800);")

    next_button = 1
    while next_button:
        next_button = driver.find_element_by_xpath(get_xpath(shop, 'next'))
        try:
            next_button.click()
        except ElementClickInterceptedException:

            driver.execute_script("arguments[0].click();", next_button)


        try:
            driver.find_element_by_xpath(get_xpath(shop, 'next_disabled'))
            next_button = None
        except NoSuchElementException:
            pass

    product_urls = []
    for p in driver.find_elements_by_xpath(get_xpath(shop, 'products')):
        product_urls.append(p.get_attribute('href'))

    products_collection = []
    for url in product_urls:
        product_info = defaultdict(str)
        driver.get(url)
        product_info['title'] = driver.find_element_by_xpath(shop.get('product_title')).text
        product_info['price'] = driver.find_element_by_xpath(shop.get('product_price')).text.replace(' ', '')
        product_info['link'] = url


        if params_link := shop.get('params_link', None):
            try:
                driver.find_element_by_xpath(params_link).click()
            except NoSuchElementException:
                break


            keys = []
            for k in driver.find_elements_by_xpath(shop.get('product_keys')):
                keys.append(k.text)
            values = []
            for n, k in enumerate(driver.find_elements_by_xpath(shop.get('product_values'))):
                values.append(k.text.replace( keys[n], ''))
            for k, v in zip(keys, values):
                product_info[k] = v

        products_collection.append(product_info)


    client = MongoClient('127.0.0.1', 27017)
    db = client['Lesson_5']
    collection = db[shop.get('name')]
    collection.insert_many(products_collection)

driver.close()
