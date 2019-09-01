import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url)

# response = requests.get(url, headers={"Accept": "text/plain"})

# print(response.text) 

response = requests.get(url, headers={"Accept": "application/json"})

# print(response.text) # it give a python string "{ ... }"
data = response.json() 

# print(type(data))
# print(data)
print(data["joke"])
print(f"status: {data['status']}")