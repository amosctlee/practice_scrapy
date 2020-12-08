import scrapy


class PttSpider(scrapy.Spider):
    name = 'ptt'

    start_urls = ['https://www.ptt.cc/bbs/NTU_Beauty/index.html']

    def parse(self, response):
        ntu_beauty = response.css(".r-list-container")
        for title_href in ntu_beauty.css(".r-ent .title a"):

            yield {
                "link": response.urljoin(title_href.css("::attr(href)").get()),
                "title": title_href.css("::text").get()
            }
