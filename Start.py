import requests
import scrapy
import ScrapyStart

useragent = {"User-Agent":""}# edit this
url = ''#edit this

def startofscript():
    # website
    session = requests.session()
    request = session.get(url)
    #status code
    status = request.status_code
    #execution
    if status == 200:
        print('OK\n')
        ScrapyStart.start()
        print('Done')

startofscript()