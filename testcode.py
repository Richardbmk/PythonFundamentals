import requests 
from bs4 import BeautifulSoup as bauty
import re

# response = requests.get('https://datosmacro.expansion.com/')
# # print(response)
# # print(response.text)

# html = response.text

# macro = bauty(html, "html.parser")

# menu = macro.select('.menu')

# head_menu = menu[-2]
# head_menu

# head_menu.select('.leaf')

# # print(head_menu.text)

# # print(head_menu.find("a")["href"])
# print('###################')
# links = head_menu.find_all('a')


# menu = macro.select('.menu')
""" 
for link in links:
    print(link.get('href'))
    print(link.text)
 """
 
print('###################')

response = requests.get('https://datosmacro.expansion.com/pib/espana')


html = response.text

macro = bauty(html, "html.parser")

pib_spain = macro.select('.col-sm-6')
pib_spain = pib_spain[2].find_all('tr')
# print(pib_spain[1].find_all('td'))
print(pib_spain)

""" for tr in pib_spain[1:]:
    tds = tr.find_all('td')
    print(tds[0].text + "," + tds[1].text + "," + tds[3].text)
 """

"""Using writer"""
""" 
from csv import writer

with open("filesio/pib_spain.csv", "w") as file:
    csv_writer = writer(file, lineterminator ="\n")
    csv_writer.writerow(["fecha", "pib_anual", "var_pib"])
    for tr in pib_spain[1:]:
        tds = tr.find_all('td')
        fecha = tds[0].text
        pib_anul = tds[1].text
        var_pib = tds[3].text
        csv_writer.writerow([fecha, pib_anul, var_pib])


 """


