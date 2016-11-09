import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'mysmartprice'

    start_urls = [
    'http://www.mysmartprice.com/fashion/filters/filter_get_redesign?subcategory=casual-shirts-clothing-men&start=24&rows=2'
    ]

    def parse(self, response):
        # follow links to author pages
        for product in response.css('div.prdct-item'):
            yield scrapy.Request('http://www.mysmartprice.com'+response.urljoin(product.css('a.prdct-item__img-wrpr::attr(href)').extract_first()),
                                  callback=self.parse_productDetails)

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
        yield {
            'name':extract_with_css('div.exthead h1.exth1::text'),
            'link': extract_with_css('div.mer-box1 a::attr(onclick)'),
            'stores': str(stores),
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
        stores = []

        urls = response.css('div.Prices').css('li.cp-c6 a::attr(onclick)').extract()

        for count in range(len(urls)):
            url = str(urls[count])
            url = url[url.find('(') + 2:]
            stores.append(url)
        return stores
