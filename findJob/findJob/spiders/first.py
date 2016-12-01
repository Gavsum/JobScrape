import scrapy
import re
import urlparse
from scrapy_splash import SplashRequest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request
from scrapy.loader import ItemLoader
from findJob.items import jobPostItem


class first(scrapy.Spider):
    name = "jobs"
    start_urls = ['https://www.careerbeacon.com/search/developer-jobs-in/',]
    BASE_URL = 'https://www.careerbeacon.com'
    items = []
    
    def parse(self, response):
        counter = 0
        hitWords = ['Developer', 'Programmer',]
        for url in self.start_urls:
            yield SplashRequest(url, args={
                'wait':2
                },)
        articles = response.xpath('//*[@id="desktop_results"]/ul')
        for p in articles.xpath('//article'):
            if (counter < 4):
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
        self.logger.info("Visited %s", response.url)
        item = jobPostItem()
        infoCount = 0
        for p in response.xpath('//*[@id="posting-body"]/article/header/div[2]/*/text()'):
            if p:
                infoCount = infoCount + 1
                #Clean format
                p = p.extract()
                p = p.lstrip()
                p = p.rstrip()
                p = p.replace('\n', '')
                p = re.sub(' +', ' ', p)

                if(infoCount == 1):
                    item['jobTitle'] = p
                elif(infoCount == 2):
                    item['sector'] = p
                elif(infoCount == 3):
                    item['company'] = p
                elif(infoCount == 4):
                    item['jobLocation'] = p
                else:
                    continue

        #print item
        count = 0
        print("\n")
        item['zPageData'] = []
        #for each entry in the page's article
        for entry in response.xpath('//*[@id="posting-body"]/article/*'):
            count = count +1
            if count > 2:
                p = entry.xpath('.//text()')
                if p:
                    p = p.extract()
                    for i in xrange(len(p)):
                        p[i] = p[i].strip(' \n\r\t')

                    item['zPageData'].append(p)

        item['zPageData'].pop()

        for key in item['zPageData']:
            for p in key:
                if p == '':
                    key.remove(p)

        return item



#Got data from page, can send to json object.
#Issue now is that while I can format the data in the dict nested in the item using strip
# as shown above, it does not seem to be written to the dict data itself and only 
# effects the print output
# Also it seems a bit clunky to be accessing nested elements like this, python probably
# has a better way.
# Lastly, it might be better to be cleansing the data on its way in as apposed to after
# its already in the item
