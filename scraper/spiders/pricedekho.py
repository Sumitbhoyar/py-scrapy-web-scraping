import scrapy

class PriceDekhoSpider(scrapy.Spider):
    name = 'pricedekho'
    counter=1
    urld =''

    def __init__(self, domain=None, category=""):
        self.allowed_domains = ['www.pricedekho.com']
        self.urld = category+'?resultonly=true&page=%d'
        self.start_urls = [
            self.urld % 1,
        ]
    # price = 0
    def parse(self, response):
        self.counter += 1

        products = response.css('#pdproductlistview > div.listingpage > ul > li > div.pd_list_link')
        if len(products) == 0:
            print('its final link')
            return
        for product in products:
            price = 0
            priceCss = product.css('div.prdt-listview > div.new-price::text').extract()[1]
            if priceCss is None:
                price = None
            else:
                price = priceCss.encode('utf-8').strip()
            yield scrapy.Request(response.urljoin(product.css('div.prdt-img > a::attr(href)').
                    extract_first()), callback=self.parse_productDetails, meta={'price': price})
            # break
        # follow pagination links
        next_page = self.urld % self.counter
        yield scrapy.Request(next_page, callback=self.parse)

    def parse_productDetails(self, response):
        def extract_with_css(query):
            productDetailsCss = response.css(query).extract_first()
            if productDetailsCss is None:
                return None
            else:
                return productDetailsCss.strip()

        price = response.meta.get('price')

        stores = self.getStores(response)
        productDetails = self.getProductDetails(response)
        reviews = self.getReviews(response)
        imageurl = response.css('a.simpleLens-thumbnail-wrapper img::attr(src)').extract()
        if len(imageurl) == 0:
            imageurl = response.css('p.nsml img::attr(src)').extract()
        yield {
            'name':extract_with_css('#overview_section > div > div.product-right-block.fleft > h1::text'),
            'link': extract_with_css('div.mer-box1 a::attr(onclick)'),
            'stores': str(stores),
            'reviews': reviews,
            'productDetails': str(productDetails),
            'image_urls': imageurl,
            'price': price,
        }

    def getProductDetails(self, response):

        detailsHeader=None
        productDetailsSection={}
        for props in response.css('#specification_section > div > div.category_detail > div > dl > dd > div > div > ul > li'):
            prop = props.css('li > span')
            productDetails = {}
            prop_key = prop[0].css('::text').extract_first().encode('utf-8')
            prop_value = prop[1].css('::text').extract_first().encode('utf-8')

            productDetails[prop_key] = prop_value
            productDetailsSection[detailsHeader] = productDetails
        return productDetailsSection

    def getStores(self, response):
        stores = {}

        pricesDiv = response.css('div.Pricesnew')

        priceElements = pricesDiv.css('#suppliers > li > div > div')
        for element in priceElements:
            store={}
            # element = priceElements[count]
            url = element.css('li.cp-c6 a::attr(onclick)').extract_first().encode('utf-8').strip()
            # url = str(urls[count])
            # rating = element.css('li.cp-c2 img::attr(src)').extract_first().encode('utf-8').strip()
            stores[url.split(',', 4)[3].replace("'", '')] = store
            url = url[url.find('(') + 2:]
            url = url[:url.find("'")]
            store['url'] = url
            # store['rating']=rating

        return stores

    def getReviews(self, response):
        reviews = {}
        for review in response.css('div.exit-rating-box'):
            store = review.css('img::attr(src)').extract_first().encode('utf-8').strip()
            store = store[store.rfind('/')+1:]
            store = store[:store.rfind('.')]
            reviews[store]=review.css('p.rate *::text').extract_first().encode('utf-8').strip()
        return reviews