import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = 'mercadolivre'

    def __init__(self, keyword='', **kwargs):
        self.start_urls = [f'https://lista.mercadolivre.com.br/{keyword}']
        super().__init__(**kwargs)

    def parse(self, response, **kwargs):
        # Declaração dos seletores css
        SELETOR_ITEMS = '//li[@class="ui-search-layout__item"]'
        SELETOR_TITLE = './/h2[contains(@class, "ui-search-item__title")]/text()'
        SELETOR_PRICE = './/span[@class="price-tag-fraction"]/text()'
        SELETOR_CENTS = './/span[@class="price-tag-cents"]/text()'

        # Monta a estrutura do json
        for pesquisa in response.xpath(SELETOR_ITEMS):
            title = pesquisa.xpath(SELETOR_TITLE).get()
            price = pesquisa.xpath(SELETOR_PRICE).get()
            cents = pesquisa.xpath(SELETOR_CENTS).get()
            cents = cents if cents else "00"
            price = f"{price},{cents}"

            yield {
                'title': title,
                'price': price,
            }

        # Busca a página seguinte enquanto existir itens
        next_page = response.xpath('//a[contains(@title, "Seguinte")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

