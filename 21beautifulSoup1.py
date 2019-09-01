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

""" 330. Navigating With BeautifulSoup """

# data1 = soup.body.contents
# data2 = soup.body.contents[1]
# data3 = soup.body.contents[1].contents
# print(data1)
# print(data3)

# data = soup.body.contents[1].next_sibling.next_sibling
# print(data)

# data1 = soup.find(class_="special")
# data2 = soup.find(class_="special").parent
# data3 = soup.find(class_="special").parent.parent
# print(data3)

# data1 = soup.find(id="first")
# data2 = soup.find(id="first").find_next_sibling()
# data3 = soup.find(id="first").find_next_sibling().find_next_sibling()
# print(data3)


# data1 = soup.select("[data-example]")
# data2 = soup.select("[data-example]")[1]
# data3 = soup.select("[data-example]")[1].find_previous_sibling()
# print(data3)

# data = soup.find(class_="super-special").find_next_sibling(class_="super-special")

data1 = soup.find("h3")
data2 = soup.find("h3").find_parent()
# print(data2)
help(data1)
