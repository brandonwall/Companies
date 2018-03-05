import scrapy
import json

  

class CompanySpider(scrapy.Spider):

    name = "company_spider"
    start_urls = ['http://corporate.northwestern.edu/highlighted-partnerships/index.html']

    def parse(self, response):
        SET_SELECTOR = '//*[@id="main-content"]'


        for coset2 in response.xpath(SET_SELECTOR):
            TABLE_SELECTOR = 'strong::text'
            yield{
                'corp_spons' : coset2.css(TABLE_SELECTOR).extract(),
                #'friend_level': coset2.xpath('//table[1]/tbody/tr/td/text()').extract(),
                #'details': coset2.css('p::text').extract(),
                #'details': coset2.xpath('.//p/text()').extract(),
                #'bullets': coset2.xpath('.//ul/li/text()').extract()
                #'silver_comp_plans': coset2.xpath('.//ul[7]/li/text()').extract(),
                #'bronze_comp_plans': coset2.xpath('.//p[46]/text()').extract(),
                # 'mega': coset2.xpath('//*[@id="partners"]/div/div/div[5]/div/div/div/table/tbody/tr/td/div/span/a/text()').extract(),
                #'kilo': coset2.xpath('//*[@id="partners"]/div/div/div[7]/div/div/div/table/tbody/tr/td/div/span/a/text()').extract(),
             }


            
'''for coset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'li::text '
            NAME_SELECTOR2 = 'a::text '

            yield {
                'name': coset.css(NAME_SELECTOR).extract_first(),
                'name2':coset.css(NAME_SELECTOR2).extract_first(),
                
            }'''


