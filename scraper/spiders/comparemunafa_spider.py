import scrapy
from selenium import webdriver

class QuotesSpider(scrapy.Spider):
    name = "munafa"
    start_urls = [
        'http://www.xmlsoft.org/FAQ.html',
    ]

    def __init__(self):
        print('12345')
        self.driver = webdriver.Chrome('/home/sumit/bin/chromedriver')
        # self.driver.wait = WebDriverWait(self.driver, 5)


    def parse(self, response):
        print('---------------++++++++---------' + response.url)
        self.driver.get(response.url)
