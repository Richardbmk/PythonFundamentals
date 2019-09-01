# 229. Sending Requests with Params

# http://www.example.com/?key1=value1&key2=value2

""" 
https://www.google.com/search?
source=hp&ei=i405XevPJcmFjLsPi-ayoAw&
q=richard+branson&
oq=Richar+br&
gs_l=psy-ab.3.0.0i10l10.2072933.2075465..2077321...2.0..0.328.2304.1j2j6j1......0....1..gws-wiz.....10..35i39j0i131j0.1izIV0_KW-I
"""

"""
# Option 1 

import requests 

response = requests.get(
"http://www.example.com?key1=value1&key2=value2")

# option 2 - preferable!

import requests

response = requests.get(
	"http://www.example.com", 
	params={
		"key1": "value1",
		"key2": "value2"
	}
)
"""

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url,
 	headers={"Accept": "application/json"},
 	# params={"term": "cat"}
 	params={"term": "cat", "limit": 2}
)


data = response.json() 

# print(data)
print(data["results"])