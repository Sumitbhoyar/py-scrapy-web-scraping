import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'smart'
    counter=1
    urld =''

    def __init__(self, domain=None, category=""):
        self.allowed_domains = ['www.mysmartprice.com']
        self.urld = 'http://www.mysmartprice.com/fashion/filters/filter_get_redesign?subcategory='+category+'&start=%d&rows=24'
        self.start_urls = [
            self.urld % 1,
        ]
    # price = 0
    def parse(self, response):
        self.counter += 24

        # follow links to author pages
        products = response.css('a.prdct-item__name::attr(href)').extract()
        if len(products) == 0:
            print('its final link')
            return
        for product in products:
            productLink = 'http://www.mysmartprice.com' + product.encode('utf-8')
            print(productLink)
            yield scrapy.Request(productLink, callback=self.parse_productDetails)
            # break
        # follow pagination links
        ##next_page = self.urld % self.counter
        ##yield scrapy.Request(next_page, callback=self.parse)

    def parse_productDetails(self, response):

        price = response.css('body > div.body-wrpr.clearfix > div:nth-child(2) > div.sctn.prdct-dtl.clearfix > div.prdct-dtl__rght > div > div.prdct-dtl__str-wrpr > div > div.prdct-dtl__prc > span:nth-child(2)::text').extract_first().encode('utf-8')
        print('Price------------' + price)
        stores = self.getStores(response)
        productDetails = self.getProductDetails(response)
        # reviews = self.getReviews(response)
        imageurl = response.css('img.prdct-dtl__thmbnl-img::attr(data-image)').extract()
        if len(imageurl) == 0:
            imageurl = response.css('img.prdct-dtl__img::attr(data-image)').extract()
        yield {
            'name':response.css('body > div.body-wrpr.clearfix > div:nth-child(2) > div > div.prdct-dtl__rght > h1::text').extract_first().encode('utf-8').strip(),
            # 'link': extract_with_css('div.mer-box1 a::attr(onclick)'),
            'stores': str(stores),
            # 'reviews': reviews,
            'productDetails': str(productDetails),
            'image_urls': imageurl,
            'price': price,
        }

    def getProductDetails(self, response):
        productDetailsSection={}
        productDetails = {}
        for attr in response.css('tr.tchncl-spcftn__item'):
            key = attr.css('td::text').extract()[0].encode('utf-8').strip()
            value = attr.css('td::text').extract()[1].encode('utf-8').strip()

            productDetails[key] = value
        productDetailsSection['TECHNICAL SPECIFICATIONS'] = productDetails
        return productDetailsSection

    def getStores(self, response):
        stores = {}

        pricesDiv = response.css('div.Pricesnew')
        price = response.css(
            'body > div.body-wrpr.clearfix > div:nth-child(2) > div.sctn.prdct-dtl.clearfix > div.prdct-dtl__rght > div > div.prdct-dtl__str-wrpr > div > div.prdct-dtl__prc > span:nth-child(2)::text').extract_first().encode(
            'utf-8')
        link = response.css('div.js-prc-tbl__gts-btn::attr(data-url)').extract_first().encode('utf-8').strip()
        link = link[link.find('url') + 4:]
        storeName=response.css('span.prdct-dtl__str-ftr--hghlght::text').extract()[2].encode('utf-8').strip()
        store = {}
        stores[storeName] = store
        store['url'] = link

        priceElements = response.css('body > div.body-wrpr.clearfix > div:nth-child(2) > div.algn-wrpr.clearfix > div.main-wrpr.algn-left > div:nth-child(1) > div > div > div.clearfix')
        for element in priceElements:
            store={}
            storeName = element.css('div > img::attr(alt)').extract_first().encode('utf-8').strip()
            # element = priceElements[count]
            url = element.css('li.cp-c6 a::attr(onclick)').extract_first().encode('utf-8').strip()
            price=element.css('span.prc-grid__prc-val::text').extract_first().encode('utf-8').strip().replace('\xe2\x82\xb9','')
            url = stores[0].css('div.prc-grid__gts-btn--mdl--ncCompare::attr(data-url)').extract_first().encode('utf-8').strip()
            url = url[url.find('url') + 4:]
            # rating = element.css('li.cp-c2 img::attr(src)').extract_first().encode('utf-8').strip()
            stores[storeName] = store
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