# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
import csv
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

with open("filesio/Blod_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        # print(article.find("a"))
        # print(article.find("a").get_text())
        # title = article.find("a").get_text()
        # print(article.find("a")["href"])
        a_tag = article.find("a")
        title = a_tag.get_text()
        # print(a_tag["href"])
        url = a_tag["href"]
        # print(article.find("time")["datetime"])
        date = article.find("time")["datetime"]
        # print(title + "," + url + "," + date)
        csv_writer.writerow([title, url, date])
