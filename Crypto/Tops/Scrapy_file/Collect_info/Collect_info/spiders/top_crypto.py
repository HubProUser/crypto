import scrapy

choose = input('gainers / losers\n')


class TopCryptoSpider(scrapy.Spider):
    name = 'tops'
    allowed_domains = ["crypto.com"]
    start_urls = ["https://crypto.com/price/showroom"]
    if choose == 'gainers':
        custom_settings = {
            'FEEDS': {'gainers.csv': {'format': 'csv'}}
        }
    if choose == 'losers':
        custom_settings = {
            'FEEDS': {'losers.csv': {'format': 'csv'}}
        }

    def parse(self, response):
        if choose == 'gainers':
            top_gainers_names = response.css('div.css-y9xirv div.css-11erl2j div.css-1v8x7dw tr.top-panel__table-row.css-vdogor td.css-65matt p.chakra-text.css-1nx08c9::text').extract()
            top_gainers_icon = response.css('div.css-y9xirv div.css-11erl2j div.css-1v8x7dw tr.top-panel__table-row.css-vdogor td.css-65matt p.chakra-text.css-1geoadh::text').extract()
            top_gainers_prices = response.css('div.css-y9xirv div.css-11erl2j div.css-1v8x7dw tr.top-panel__table-row.css-vdogor td.css-1d4ilmx p.chakra-text.css-cd7o48::text').extract()
            top_gainers_persantage = response.css('div.css-y9xirv div.css-11erl2j div.css-1v8x7dw tr.top-panel__table-row.css-vdogor td.css-8ndcyp p.chakra-text.css-kakntk::text').extract()
            for item in zip(top_gainers_names, top_gainers_icon, top_gainers_prices, top_gainers_persantage):
                top_gainers = {
                    "name": item[0],
                    "icon": item[1],
                    "price": item[2],
                    "grow": item[3],
                }
                yield top_gainers

        if choose == 'losers':

            top_losers_names = response.css('div.css-1gioywb div.css-1v8x7dw table.chakra-table.css-5605sr tr.top-panel__table-row.css-vdogor div.css-k008qs p.chakra-text.css-1nx08c9::text').extract_first()
            top_losers_icon = response.css('div.css-1gioywb div.css-1v8x7dw table.chakra-table.css-5605sr tr.top-panel__table-row.css-vdogor div.css-k008qs p.chakra-text.css-1geoadh::text').extract()
            top_losers_prices = response.css('div.css-1gioywb div.css-1v8x7dw table.chakra-table.css-5605sr tr.top-panel__table-row.css-vdogor td.css-1d4ilmx p.chakra-text.css-cd7o48::text').extract()
            top_losers_persantage = response.css('div.css-1gioywb div.css-1v8x7dw table.chakra-table.css-5605sr tr.top-panel__table-row.css-vdogor td.css-8ndcyp p.chakra-text.css-1waheym::text').extract()
            for item in zip(top_losers_names, top_losers_icon, top_losers_prices, top_losers_persantage):
                top_losers = {
                    "name": item[0],
                    "icon": item[1],
                    "price": item[2],
                    "lost": item[3],
                }
                yield top_losers
