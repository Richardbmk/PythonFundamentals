# http://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
	name = "BookSpider"
	start_urls = ["http://books.toscrape.com/"]

	def parse(self, response):
		for article in response.css("article.product_pod"):
			yield {
				"price": article.css(".price_color::text").extract_first(),
				"title": article.css("h3 > a::attr(title)").extract_first(),
			}

			# next = response.css(".next > a::attr(href)").extract_first()
			# if next:
			# 	yield response.follow(next, self.parses)


scrapy runspider -o books.csv scrapyProject.py



# scrapy runspider -o books.csv 23scrapyProject.py
# scrapy runspider -o filesio/books.csv 23scrapyProject.py
# scrapy runspider -o books.json 23scrapyProject.py
# scrapy runspider -o filesio/books.json 23scrapyProject.py