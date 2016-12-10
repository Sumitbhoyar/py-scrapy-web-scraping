import scrapy


class QuotesSpider(scrapy.Spider):
    name = "category"
    start_urls = [
        'https://www.compareraja.in/all-categories.html',
    ]

    def parse(self, response):
        for category in response.css('#LayoutDiv1 > section > div > div > ul > li > a'):
            yield scrapy.Request(category.css('a::attr(href)').extract_first().encode('utf-8').strip(),
                                 callback=getcategory,
                                 meta={'category': category.css('*::text').extract_first().encode('utf-8').strip()})


def getcategory(response):
    yield {
        'category': response.meta.get('category'),
        'id': response.css('#hdncategoryid::attr(value)').extract_first().encode('utf-8').strip(),
    }
