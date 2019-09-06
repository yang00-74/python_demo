import  scrapy
# import the containner 
from scrapy_project.items import ScrapyProjectItem

class LittleSpider(scrapy.Spider):
    name = "little" #the name is unique 
    allowed_domains = ['taobao.com']
    start_urls = [
        'https://www.taobao.com/',
    ]

    def parse(self,response):
        # filename = "".join([response.url.split(".")[-2],".txt"])
        # filename = response.url.split(".")[-2]
        # print("the file is %s"%filename)
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        selector = scrapy.selector.Selector(response)
        sites = selector.xpath('//ul/li')
        lis = []
        for site in sites:
            item = ScrapyProjectItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            lis.append(item)
       
        return lis

        