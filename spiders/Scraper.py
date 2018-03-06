import scrapy
import json

  

class CompanySpider(scrapy.Spider):

    name = "company_spider"
    start_urls = ['https://www.engineering.uiowa.edu/economic-partners/strengthening-business-alliance-university-iowa-college-engineering#Experiential']

    def parse(self, response):
        SET_SELECTOR = '//*[@id="main"]/div/div/div/div/div/div/div/div/div/div/div/article/div/div/div/div'


        for coset2 in response.xpath(SET_SELECTOR):
            TABLE_SELECTOR = 'h3::text'
            SEC_SELECTOR = 'a::text'
            CO_SELECTOR = 'p::text'
            yield{
                'other_ops': coset2.css(SEC_SELECTOR).extract(),
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


