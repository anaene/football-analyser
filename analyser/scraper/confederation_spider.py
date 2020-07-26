import scrapy


class ConfederationSpider(scrapy.Spider):
    name = "confederations"

    start_urls = [
        'https://www.fifa.com/associations/caf/'
    ]

    def parse(self, response):
        region_header = response.css('ul.fi-main-menu')
        confederation_header = response.css('div.fi-ah__association__name')
        associations = response.css('div.fi-association-card')
        yield {
            'name': confederation_header.css('span.fi-a__nDesc::text').get(),
            'region': region_header.css('a.active::text').get().strip(),
            'abbreviation': confederation_header.css('span.fi-a__nText::text').get(),
            'association_countries': associations.css('span.fi-a__nText::text').getall(),
        }

        for href in region_header.css('li a::attr(href)'):
            yield response.follow(href, self.parse)
