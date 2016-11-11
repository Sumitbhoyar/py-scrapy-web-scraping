import scrapy


class ProxySpider(scrapy.Spider):
    name = "proxy"
    domain_name = "checkip.dyndns.org"
    start_urls = ["http://checkip.dyndns.org/",
                  "http://checkip.dyndns.org/",
                  "http://checkip.dyndns.org/",
                  "http://checkip.dyndns.org/",
                  "http://checkip.dyndns.org/",
                  "http://checkip.dyndns.org/",
                  ]

    def parse(self, response):
        yield {
            'proxy' : response.xpath('//body/text()').re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')[0]
        }
