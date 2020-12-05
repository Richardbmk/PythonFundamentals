import requests 
import json

HEADERS = {'Accept': 'application/json; application/vnd.esios-api-v1+json',
           'Content-Type': 'application/json',
           'Host': 'api.esios.ree.es',
           'Authorization': 'Token token="77ea0584ba185e021684320f55458362c56efe3c73ab0c89a3a38510f2bacccc"'
}




response = requests.get(
    'https://api.esios.ree.es/indicators/1013?start_date=2020-08-22T00:00:00&end_date=2020-08-22T23:50:00',
    headers=HEADERS,
)

print(response)
print(response.json())
""" 
json_data = response.json()

pretty_data = json.dumps(json_data, indent=2)

print(pretty_data) """