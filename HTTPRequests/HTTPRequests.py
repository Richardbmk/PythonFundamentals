"""
HTTP (HyperText Transfer Protocol ) Introduction
"""
# python -m pip install requests

import requests 
# res = requests.get("https://github.com/")
# res 
# res.ok 
# res.headers 
url = "https://www.google.com/"

response = requests.get(url)

# print(f"your reques to {url} came back w/ status code {response.status_code}")
# print(response.text)

