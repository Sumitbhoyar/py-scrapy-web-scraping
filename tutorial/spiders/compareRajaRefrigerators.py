import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'crRefrigerator'

    start_urls = [
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=1&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=2&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=3&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=4&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=5&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=6&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=7&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=8&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=9&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=10&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=11&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=12&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=13&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=14&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=15&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=16&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=17&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=18&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=19&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=20&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=21&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=22&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=23&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=24&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=25&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=26&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=27&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=28&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=29&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
        'https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=30&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam=',
    ]

    def parse(self, response):
        # follow links to author pages
        for product in response.css('article.product'):
            yield scrapy.Request(response.urljoin(product.css('a::attr(href)').extract_first()),
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
        link = extract_with_css('div.mer-box1 a::attr(href)')
        id = link[link.rfind('/')+1:]
        yield {

            'id': id,
            'name':extract_with_css('div.exthead h1.exth1::text'),
            'url': extract_with_css('div.mer-box1 a::attr(onclick)'),
            'stores': str(stores),
            'productDetails': str(productDetails),
            'image_urls': response.css('a.simpleLens-thumbnail-wrapper img::attr(src)').extract(),
        }

    def getProductDetails(self, response):
        productDetails = {}
        for details in response.css('ul.fedet'):
            for attr in details.css('li'):

                key = attr.css('p::text').extract_first()
                if key is None:
                    continue
                value = attr.css('span::text').extract_first()

                print("---------------------" + key)
                print("---------------------" + value)
                productDetails[key.encode('utf-8').strip()] = value.encode('utf-8').strip()
        return productDetails

    def getStores(self, response):
        stores = {}
        cssStore = response.css('div.Prices')

        prices = cssStore.css('li.cp-c5 span::text').extract()
        urls = cssStore.css('li.cp-c6 a::attr(onclick)').extract()

        for count in range(len(urls)):
            aStore = {}
            url = str(urls[count])
            aStore['price'] = str(prices[count*2+1])
            aStore['url'] = url
            url = url[url.find('//')+2:]
            url = url[:url.find('/')]
            stores[url] = aStore
        return stores
