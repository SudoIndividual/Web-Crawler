import scrapy
from scrapy.crawler import CrawlerProcess
#spider
class ScrapyReference(scrapy.Spider):
    name = "projectcrawl"
    allowed_domains = ['']#edit this
    start_urls = [
        ''
    ]#edit this
    list_url = []
    def parse(self, response):
        url = response.url
        
        for items in response.css("a::attr(href)").extract():
            if "http" in items:
                self.list_url.append(items)
            else:
                self.list_url.append(url + '/'+ items)
            if items is not None:
                yield response.follow(items,self.parse)
        
        reference_file=open('Extract/Redirection.txt','w+')
        duplicate_remove = list(dict.fromkeys(self.list_url))
        file_input = (((str(duplicate_remove)[1:-1])).replace(",","\n",-1))
        reference_file.write(file_input)

        reference_file.close()