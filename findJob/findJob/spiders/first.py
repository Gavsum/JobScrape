import scrapy
import re
import urlparse
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request


class first(scrapy.Spider):
    name = "jobs"
    start_urls = ['https://www.careerbeacon.com/search/developer-jobs-in/',]
    BASE_URL = 'https://www.careerbeacon.com'
    
    def parse(self, response):
        counter = 0
        hitWords = ['Developer', 'Programmer',]
        for url in self.start_urls:
            yield SplashRequest(url, args={
                'wait':5
                },)
        articles = response.xpath('//*[@id="desktop_results"]/ul')
        for p in articles.xpath('//article'):
            if (counter < 3):
                x = p.xpath('.//div[3]/a/div[1]/h2/text()')
                for title in x:
                    b = re.sub(ur'[^\w]', ' ', title.extract()).strip()
                    for hit in hitWords:
                        if hit in b:                       
                            pageData = p.xpath('.//a/@href').extract()
                            absoluteUrl = self.BASE_URL + pageData[1]
                            counter = counter + 1
                            yield Request(url=absoluteUrl, callback=self.getData)

    def getData(self, response):
        print("\n")
        self.logger.info("Visited %s", response.url)
        test = response.xpath('//title/text()')
        print(test)
        print("\n")


#Access of both title and link element from page items is working
#Now need to either collect all the links for accessing later, or 
#Figure out how to access each link sequentially and scrape data off of the relevant page
