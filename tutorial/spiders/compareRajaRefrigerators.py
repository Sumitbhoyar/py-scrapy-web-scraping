import scrapy
from scrapy import Request


class AuthorSpider(scrapy.Spider):
    name = 'crRefrigerator'

    start_urls = [
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=1&categoryId=10&CategoryNameInURLs=refrigerators&catid=10&catname=refrigerators',
    ]

    def start_reqests(self):
        print ('calling ..........................................')
        yield Request('http://checkip.dyndns.org/', callback=self.check_ip)
        # yield other requests from start_urls here if needed

    def check_ip(self, response):
        print(str(response))


    def parse(self, response):
        print('`````````````````````````````````````')
        self.start_reqests()
        print('`````````````````````````````````````')
        # follow links to author pages
        for product in response.css('article.product'):
            yield scrapy.Request(response.urljoin(product.css('a::attr(href)').extract_first()),
                                  callback=self.parse_productDetails)
            break

        # follow pagination links
        # next_page = response.css('article.load-more a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_productDetails(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        stores = self.getStores(response)
        productDetails = self.getProductDetails(response)
        reviews = self.getReviews(response)
        yield {
            'name':extract_with_css('div.exthead h1.exth1::text'),
            'link': extract_with_css('div.mer-box1 a::attr(onclick)'),
            'stores': str(stores),
            'reviews': reviews,
            'productDetails': str(productDetails),
            'image_urls': response.css('a.simpleLens-thumbnail-wrapper img::attr(src)').extract(),
        }

    def getProductDetails(self, response):

        detailsHeader=None
        productDetailsSection={}
        for details in response.css('ul.fedet'):
            productDetails = {}
            for attr in details.css('li'):
                key = attr.css('p::text').extract_first()
                if key is None:
                    detailsHeader = attr.css('::text').extract_first().encode('utf-8').strip()
                    continue
                value = attr.css('span::text').extract_first()

                productDetails[key.encode('utf-8').strip()] = value.encode('utf-8').strip()
            productDetailsSection[detailsHeader]=productDetails
        return productDetailsSection

    def getStores(self, response):
        stores = {}

        pricesDiv = response.css('div.Pricesnew')

        priceElements = pricesDiv.css('ul.nemcomp-price-row-nw')
        for element in priceElements:
            store={}
            # element = priceElements[count]
            url = element.css('li.cp-c6 a::attr(onclick)').extract_first().encode('utf-8').strip()
            # url = str(urls[count])
            rating = element.css('li.cp-c2 img::attr(src)').extract_first().encode('utf-8').strip()
            stores[url.split(',', 4)[3].replace("'", '')] = store
            url = url[url.find('(') + 2:]
            url = url[:url.find("'")]
            store['url'] = url
            store['rating']=rating

        return stores

    def getReviews(self, response):
        reviews = {}
        for review in response.css('div.exit-rating-box'):
            store = review.css('img::attr(src)').extract_first().encode('utf-8').strip()
            store = store[store.rfind('/')+1:]
            store = store[:store.rfind('.')]
            reviews[store]=review.css('p.rate *::text').extract_first().encode('utf-8').strip()
        return reviews