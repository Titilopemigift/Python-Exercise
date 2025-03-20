import requests

response= requests.get('http://api.football-data.org/v4/competitions/') 
response.status_code

response.json()

response.json().keys()

data= response.json()["competitions"]
data

competition_names = [item["name"] for item in data]
print(competition_names)