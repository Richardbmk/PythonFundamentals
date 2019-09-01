""" A Solution for scraping all the pages in the blog
SOLUTION OFERED BY A COLLAGE """


# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
import csv
from csv import writer

with open("filesio/Blod_Alldata.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    page = 1
    while True:
        response = requests.get("https://www.rithmschool.com/blog?page=" + str(page))
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")
        if articles:
            for article in articles:
                a_tag = article.find("a")
                title = a_tag.get_text()
                url = a_tag["href"]
                date = article.find("time")["datetime"]
                csv_writer.writerow([title, url, date])
            page +=1
        else:
            break
