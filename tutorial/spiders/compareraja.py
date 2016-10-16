import scrapy


class QuotesSpider(scrapy.Spider):
    name = "compareraja"
    start_urls = [
        'https://www.compareraja.in/mobiles.html',
    ]

    def parse(self, response):
        for quote in response.css('article.product'):
            yield {
                'name': quote.css('a.link::attr(title)').extract_first(),
                'price': quote.css('b::text').extract_first(),
            }