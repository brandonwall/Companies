import scrapy
import json

  

class CompanySpider(scrapy.Spider):

    name = "company_spider"
    start_urls = ['https://career.ucsd.edu/employers/members.html']

    def parse(self, response):
        SET_SELECTOR = '//*[@id="main-content"]/div/section[1]/article'

        for coset2 in response.xpath(SET_SELECTOR):
            TABLE_SELECTOR = 'h3::text'
            SEC_SELECTOR = 'a::text'
            CO_SELECTOR = 'p::text'
            yield{
                'Platinum_Cos1': coset2.xpath('.//p[3]/img/@alt').extract(),
                'Platinum_Cos2': coset2.xpath('.//p[4]/img/@alt').extract(),
                'Gold_Cos': coset2.xpath('.//p[5]/img/@alt').extract(),
                'Silver_Cos1': coset2.xpath('.//p[6]/span/img/@alt').extract(),
                'Silver_Cos2': coset2.xpath('.//p[6]/img/@src').extract(),
                'Silver_Cos3': coset2.xpath('.//p[7]/span/img/@alt').extract(),
                'Silver_Cos4': coset2.xpath('.//p[8]/span/img/@alt').extract(),
                'Sml_Bus_Gov_NonProf': coset2.xpath('.//p[9]/img/@alt').extract(),
                'Reasons_to_Join': coset2.xpath('.//p[10]/text()').extract(),
                #'bullets': coset2.xpath('.//ul/li/text()').extract()
                #'silver_comp_plans': coset2.xpath('.//ul[7]/li/text()').extract(),
                #'bronze_comp_plans': coset2.xpath('.//p[46]/text()').extract(),
                # 'mega': coset2.xpath('//*[@id="partners"]/div/div/div[5]/div/div/div/table/tbody/tr/td/div/span/a/text()').extract(),
                #'kilo': coset2.xpath('//*[@id="partners"]/div/div/div[7]/div/div/div/table/tbody/tr/td/div/span/a/text()').extract(),
             }



