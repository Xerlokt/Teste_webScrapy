import scrapy


class SpiderShop(scrapy.Spider):
    name = "E_shop_spider"
    start_urls = ["https://web-scraping.dev/products"] 

    def parse(self, response):
        products = response.css('div.row.product')

        for product in products:
            yield{
                'name' : product.css('div.description h3 a::text').get(),
                'price' : product.css('div.price-wrap div.price::text').get(),
                'description' : product.css('div.short-description::text').get(),
                'image' : product.css('div.thumbnail img::attr(src)').get(),
                'link' : product.css('div.description h3 a::attr(href)').get(),
            }

        next_page = response.css('a[href*="page="]:contains(">")::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)
