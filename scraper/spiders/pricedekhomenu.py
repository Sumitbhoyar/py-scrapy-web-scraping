import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pricedekhomenu"
    start_urls = [
        'file:///home/sumit/temp/scrap.html',
    ]

    def parse(self, response):
        for level1 in response.css('body > div'):
            levelcss = level1.css('div.nav-title::text').extract_first()
            if levelcss == None:
                continue
            level1Label = levelcss.encode('utf-8').strip()
            level2Dict = {}
            for level2 in level1.css('div.categories-list'):
                level2Level = level2.css('div > a ::text').extract_first()
                if None == level2Level:
                    continue
                level2Label = level2Level.encode('utf-8')
                label2Link = level2.css('div > a ::attr(href)').extract_first().encode('utf-8')
                level3Dict = {}
                level2Dict[level2Label] = level3Dict
                level3Dict['link'] = label2Link
                for level3 in level2.css('ul > li > a'):
                    level3Label = level3.css('*::text').extract_first().encode('utf-8')
                    label3Link = level3.css('*::attr(href)').extract_first().encode('utf-8')
                    level3Dict[level3Label] = label3Link
            yield{
                level1Label: level2Dict
            }
