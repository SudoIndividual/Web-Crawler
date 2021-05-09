import scrapy

class ScrapyJPG(scrapy.Spider):
    name = "projectcrawl"
    allowed_domains = ['']#edit this
    start_urls = [
        ''
    ]#edit this
    list_url = []

    def parse(self, response):
        url = response.url
        for picture_href in response.css('img::attr(src)').extract():
            if ".jpg" in picture_href:
                self.list_url.append(url + picture_href)

        for items in response.css("a::attr(href)").extract():
            if items is not None:
                yield response.follow(items,self.parse)    

        file = open('Extract/Jpg.txt','w+')
        duplicate_remove = list(dict.fromkeys(self.list_url))
        file_input = (((str(duplicate_remove)[1:-1])).replace(",","\n",-1))
        file.write(file_input)