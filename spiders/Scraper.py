import scrapy
import json

  

class CompanySpider(scrapy.Spider):

    name = "company_spider"
    start_urls = ['https://www.cs.purdue.edu/corporate/partners/index.html']

    def parse(self, response):
        SET_SELECTOR = '.content'


        for coset2 in response.css(SET_SELECTOR):
            TABLE_SELECTOR = './/strong/text()'

            yield{
                'table': coset2.xpath(TABLE_SELECTOR).extract(),
                'friend': coset2.xpath('.//ul[2]/li/a/text()').extract(),
                'advisor': coset2.xpath('.//div/div[2]/ul[1]/li/a/text()').extract(),
             }


            
'''for coset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'li::text '
            NAME_SELECTOR2 = 'a::text '

            yield {
                'name': coset.css(NAME_SELECTOR).extract_first(),
                'name2':coset.css(NAME_SELECTOR2).extract_first(),
                
            }'''


