import requests
import pandas as pd

url = 'https://content.guardianapis.com/search?api-key=test&q=Nigeria&from-date=2025-01-01&to-date=2025-03-25&page-size=100'

baseurl = 'https://content.guardianapis.com/search'

params={
        'api-key':'test',
        'q':'Nigeria',
        'from-date': '2025-01-01',
        'to-date': '2025-03-25',
        'page-size':100
    }
response = requests.get(baseurl, params= params)
response.status_code

if response.status_code ==200:
    result= response.json()
    data = result.get('response',{}).get('results',[])
print(data)

def articles(country):
    list_of_articles=[]
    for article in country:
        if 'Nigeria' or 'nigeria' in country:
            list_of_articles.append(article)
            return list_of_articles

country = data

print(articles(country))



df = pd.DataFrame(country)
print(df)


df_country= df.to_csv('Nigeria_2025.csv', index=False)
print('csv successfully created')

df_nigeria= pd.read_csv('Nigeria_2025.csv')
print(df_nigeria)



