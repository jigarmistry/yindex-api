import scrapy
from scrapy.crawler import CrawlerProcess,CrawlerRunner
from twisted.internet import reactor

class IncomeStatementSpider(scrapy.Spider):
    name = "income_statement"
    start_urls = []
    income_sts = []

    def __init__(self, domain=None, *args, **kwargs):
        super(IncomeStatementSpider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]


    def parse(self, response):
        sel = response.selector
        rows = sel.xpath('//tr')
        for row in rows:
            row = row.xpath('td/text()').extract()
            if len(row) > 1 and row[0].strip() != "":
                self.income_sts.append(row)


def get_income_statement_wsj(country,stock,type):
    domain = "http://192.168.2.174:8080/st.html"
    incSpider = IncomeStatementSpider(domain=domain)
    runner = CrawlerRunner()
    runner.crawl(incSpider,domain=domain)
    reactor.run()
    json = {}
    for i,v in enumerate(incSpider.income_sts):
        json[i] = v

    return json
