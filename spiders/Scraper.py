import scrapy
import json

  

class CompanySpider(scrapy.Spider):

    name = "company_spider"
    start_urls = ['https://www.sice.indiana.edu/alumni-giving/giving/corporate-partners/accelerator.html']

    def parse(self, response):
        SET_SELECTOR = '//*[@id="content-wrap"]/div'


        for coset2 in response.xpath(SET_SELECTOR):
            TABLE_SELECTOR = 'h4::text'
            SEC_SELECTOR = 'strong::text'
            CO_SELECTOR = 'p::text'
            yield{
                'headings': coset2.css(TABLE_SELECTOR).extract(),
                'info': coset2.css(SEC_SELECTOR).extract(),
                'company_1_3_9': coset2.xpath('//*[@id="sidebar"]/div[2]/div/div/p/text()').extract(),
                'gift_dest': coset2.xpath('//*[@id="content"]/p/em/text()').extract(),
                'preferred_5000': coset2.xpath('//*[@id="content"]/ul[1]/li/text()').extract(),
                'premier_10000': coset2.xpath('//*[@id="content"]/ul[2]/li/text()').extract(),
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


