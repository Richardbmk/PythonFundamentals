# 366. Scraping to a Database Pt. 1
import sqlite3
import requests
from bs4 import BeautifulSoup

# Request URL
response = requests.get("http://books.toscrape.com/catalogue/page-1.html")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
#print(books)

for book in books:
    #title = book.find("h3").find("a")["title"]
    #price = book.select(".price_color")[0].get_text()
    #price = float(price.replace("£","").replace("Â", ""))
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    int_rating = ratings[rating]
    print(int_rating)
