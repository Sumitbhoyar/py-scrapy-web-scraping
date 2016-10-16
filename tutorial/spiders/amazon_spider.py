import scrapy


class QuotesSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'http://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T2?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_98%3A10440597031%2Cp_36%3A800000-1200000&bbn=1805560031&rw_html_to_wsrp=1&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-10&pf_rd_r=1C0N1MH755STYNW2BJVQ&pf_rd_t=101&pf_rd_p=03f4481d-5c79-4072-b153-a1a53892a5b5&pf_rd_i=1389401031',
        'http://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T3?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_98%3A10440597031%2Cp_36%3A1200000-1500000&bbn=1805560031&rw_html_to_wsrp=1&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-10&pf_rd_r=1C0N1MH755STYNW2BJVQ&pf_rd_t=101&pf_rd_p=03f4481d-5c79-4072-b153-a1a53892a5b5&pf_rd_i=1389401031',
    ]

    def parse(self, response):
        for quote in response.css('li.s-result-item'):
            yield {
                'id': quote.css('li.s-result-item::attr(data-asin)').extract_first(),
                'name': quote.css('h2::text').extract_first(),
                'price': quote.css('span.a-color-price::text').extract_first(),
            }