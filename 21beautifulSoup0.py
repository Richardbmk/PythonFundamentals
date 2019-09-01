from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

""" loking for HTML tags"""
# print(soup)
# print(type(soup))
# print(soup.body)
# print(soup.body.div)
# print(soup.find("div"))

# d = soup.find("div")
# print(type(d))

# print(soup.find_all("div"))

# print(soup.find(id="first"))

# print(soup.find_all(class_="special"))

# print(soup.find_all(attrs={"data-example": "yes"}))

""" loking foR CSS tags"""
# print(soup.select("#first")) # Give a list
# print(soup.select("#first")[0]) # without a list
# print(soup.select(".special"))
# print(soup.select("div"))
# print(soup.select("[data-example]"))


""" loking foR the information inside the tags"""

# el = soup.select(".special")[0]
# print(el.get_text())

# for el in soup.select(".special"):
# 	print(el.get_text())

# for el in soup.select(".special"):
# 	print(el.name)

# for el in soup.select(".special"):
# 	print(el.name)
# 	print(el.attrs) # access the atributs

attr = soup.find("h3")["data-example"]
# print(attr)

attr = soup.find("div")["id"]
# print(attr)
