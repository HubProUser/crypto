import scrapy

options = input('What to collect?\n1. Gainers\n 2. Losers\n 3. Trending\n 4. Popular among users\n')
start_url = None

if options == '1':
    start_url = 'https://crypto.com/price/showroom/biggest-gainers'
if options == '2':
    start_url = 'https://crypto.com/price/showroom/biggest-losers'
if options == '3':
    start_url = 'https://crypto.com/price/showroom/trending'
if options == '4':
    start_url = 'https://crypto.com/price/showroom/most-popular'


class ParseSpider(scrapy.Spider):
    name = "cryptocom"
    allowed_domains = ["crypto.com"]
    start_urls = start_url

    def parse(self, response):
        h24_change = None

        name = response.css('div.css-1v8x7dw tr.showroom__sub-link__table-row.css-1cxc880 td.css-1sem0fc span.chakra-text.css-eb93p1::text').extract()
        short = response.css('div.css-1v8x7dw tr.showroom__sub-link__table-row.css-1cxc880 td.css-1sem0fc span.chakra-text.css-1jj7b1a::text').extract()
        price = response.css('div.css-1v8x7dw tr.showroom__sub-link__table-row.css-1cxc880 td.css-1vyy4qg div.css-b1ilzc::text').extract()
        if options == '1':
            h24_change = response.css('div.css-1v8x7dw tr.showroom__sub-link__table-row.css-1cxc880 td.css-1vyy4qg div.css-16q9pr7 p.chakra-text.css-9wlehu::text').extract()
        if options == '2':
            h24_change = response.css('div.css-1v8x7dw tr.showroom__sub-link__table-row.css-1cxc880 td.css-1vyy4qg div.css-16q9pr7 p.chakra-text.css-bgmtjo::text').extract()
        market_cap = response.css('div.css-1v8x7dw tr.showroom__sub-link__table-row.css-1cxc880 td.css-13av8ha::text').extract()
        yield name, short, price, h24_change, market_cap
