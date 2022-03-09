from re import U
import scrapy
from itScrape.itemsB import ScrapeItem
from scrapy.loader import ItemLoader


class iSpider(scrapy.Spider):
    name = "books"

    #normal paginating trakes a lot more time
    #start_urls = [
    #    'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page='
    #]

    #faster times scraping pagse
    url = 'https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=20&page={}'

    def start_requests(self):
        for i in range(1,6):
            yield scrapy.Request(self.url.format(i))

    def parse(self, response):
        names = 'div[class*=topX-row] div.product-info-view div.product-shelf-title h3 a'
        public = 'div[class*=topX-row] div.product-info-view div.product-shelf-title h3 span'
        author = 'div[class*=topX-row] div.product-info-view div.product-shelf-author a'
        price = 'div[class*=topX-row] div.product-info-view div[class*=mt-s] table tbody tr td[class*=buy-new] span[class*=current] a'


        for items in response.css('ol[class*=product-shelf-list] li[class*=pb-s]'):
                l = ItemLoader(item = ScrapeItem(), selector = items)

                l.add_css('name', names)
                l.add_css('publication_date', public)
                l.add_css('author', author)
                l.add_css('price', price)

                yield l.load_item()


            #ol[class*=product-shelf-list] li[class*=pb-s] div[class*=topX-row] div.product-info-view div.product-shelf-title h3 a::text //book_name
            #ol[class*=product-shelf-list] li[class*=pb-s] div[class*=topX-row] div.product-info-view div.product-shelf-title h3 span::text //publication_date
            #ol[class*=product-shelf-list] li[class*=pb-s] div[class*=topX-row] div.product-info-view div.product-shelf-author a::text')[0].get() //author
            #ol[class*=product-shelf-list] li[class*=pb-s] div[class*=topX-row] div.product-info-view div[class*=mt-s] table tbody tr td[class*=buy-new] span[class*=current] a::text // price
