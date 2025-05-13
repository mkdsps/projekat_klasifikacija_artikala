import scrapy
# from bs4 import BeautifulSoup

class TechnomediaSpider(scrapy.Spider):
    name = 'technomedia'
    start_urls = ['https://tehnomedia.rs']

    def parse(self, response):
        # Pronalaženje svih 'section' elemenata sa klasom 'product-menu show'
        section = response.xpath("//section[@class='products-menu']")
        div = section.xpath("//div[@class='products-menu-sleeve']")

        for item in div.css("li"):
            # name = item.xpath(".//text()").get()
            link = item.xpath(".//@href").get()
            if (len(link.split('/')) == 5):
                yield scrapy.Request(link, callback=self._parse_sve_strane)
                break
                        
    def _parse_sve_strane(self, response):
        nesto = '?dt=1&&strana='

        div = response.xpath("//div[contains(@class, 'pagination-container')]")
        if div: #ako ima vise strana
            list_items = div.css('li')
            last_page_li = list_items[-1]

            poslednjaStrana = last_page_li.xpath(".//text()").get() #radi!


            for i in range(1,int(poslednjaStrana)+1):
                yield scrapy.Request(f'{response.url}{nesto}{i}', callback=self._parse_arikli_url)
        else: #ako ima samo jednu stranu...
            yield scrapy.Request(response.url, callback=self._parse_arikli_url)
        

    def _parse_arikli_url(self, response):
        for div in response.xpath("//div[contains(@class, 'product-single ')]"):
            k = div.xpath(".//div[contains(@class, 'product-image')]")
            a = k.css('a')
            yield scrapy.Request(a.xpath(".//@href").get(), callback=self._final)

    def _final(self, response):
        td = response.xpath("//td[contains(@class, 'feature-title')]")
        naziv = td.xpath(".//text()").get()

        li = response.xpath("//li[contains(@class, 'product-group')]")
        a = li.css('a')
        kategorija = a.xpath(".//text()").get()

        yield {"naziv": naziv,"kategorija": kategorija}



