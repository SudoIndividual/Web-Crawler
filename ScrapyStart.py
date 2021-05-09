import ScrapyReference
import ScrapyJPG
from scrapy.crawler import CrawlerProcess

def start():
    process = CrawlerProcess()
    process.crawl(ScrapyReference.ScrapyReference)
    process.crawl(ScrapyJPG.ScrapyJPG)
    process.start()