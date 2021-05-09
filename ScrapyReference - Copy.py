import scrapy

#spider
class ScrapyReference(scrapy.Spider):
    name = "projectcrawl"
    start_urls = [
        'http://172.18.58.238/index.php'
    ]

    def parse(self, response):
        url = response.url
        reference_file=open('Extract/Task 6.json','w')
        for items in response.css("a::attr(href)").extract():
            reference_file.write(str({'url': url +'/' + items})+"\n")
        reference_file.close()

