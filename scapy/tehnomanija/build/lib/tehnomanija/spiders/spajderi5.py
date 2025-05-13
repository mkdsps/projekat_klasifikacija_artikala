import scrapy
# from bs4 import BeautifulSoup

class TechnomediaSpider(scrapy.Spider):
    name = 'technomedia5'
    all_urls = ['https://www.tehnomedia.rs/bela-tehnika', 
                  'https://www.tehnomedia.rs/kucni-aparati',
                  'https://www.tehnomedia.rs/tv-video-i-foto-tehnika',
                  'https://www.tehnomedia.rs/alati-i-bastenska-oprema',
                  'https://www.tehnomedia.rs/telefonija',
                  'https://www.tehnomedia.rs/grejanje-i-klimatizacija',
                  'https://www.tehnomedia.rs/lepota-i-zdravlje',
                  'https://www.tehnomedia.rs/sport-i-rekreacija',
                  'https://www.tehnomedia.rs/pokucstvo',
                  'https://www.tehnomedia.rs/it-uredjaji'
                  ]

    # start_urls = all_urls[:2]
    # start_urls = all_urls[2:4]
    # start_urls = all_urls[4:6]
    # start_urls = all_urls[6:8]
    start_urls = all_urls[8:]



    def parse(self, response):
        # yield scrapy.Request('https://www.tehnomedia.rs/pokucstvo/rasveta', callback=self._parse_sve_strane, cb_kwargs=dict(kategorija= 'pokucstvo'))
        for item in response.xpath("//div[contains(@class,'cat-main-data')]"):
            link = item.css('a')[0].xpath('.//@href').get()
            ctgry = response.url.split('/')[-1]
            yield scrapy.Request(link, callback=self._parse_sve_strane, cb_kwargs=dict(kategorija= ctgry))
            
                        
    def _parse_sve_strane(self, response, kategorija):
        nesto = '?dt=1&&strana='

        div = response.xpath("//div[contains(@class, 'pagination-container')]")
        if div: #ako ima vise strana
            list_items = div.css('li')
            last_page_li = list_items[-1]

            poslednjaStrana = last_page_li.xpath(".//text()").get() #radi!


            for i in range(1,int(poslednjaStrana)+1):
                yield scrapy.Request(f'{response.url}{nesto}{i}', callback=self._parse_arikli_url, cb_kwargs=dict(kategorija=kategorija))
                

        else: #ako ima samo jednu stranu...
            yield scrapy.Request(response.url, callback=self._parse_arikli_url, cb_kwargs=dict(kategorija=kategorija))
            
        

    def _parse_arikli_url(self, response, kategorija):
        for div in response.xpath("//div[contains(@class, 'product-single ')]"):
            k = div.xpath(".//div[contains(@class, 'product-image')]")
            a = k.css('a')
            yield scrapy.Request(a.xpath(".//@href").get(), callback=self._final, cb_kwargs=dict(kategorija=kategorija))

    def _final(self, response, kategorija):
        td = response.xpath("//td[contains(@class, 'feature-title')]")
        naziv = td.xpath(".//text()").get()

        if not naziv:
            naziv = response.css('h1::text').get()

        yield {"naziv": naziv,"kategorija": kategorija}



