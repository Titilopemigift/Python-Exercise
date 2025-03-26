import requests
import pandas as pd


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

result= (response.json()['response']['results'])
print(result)

def articles(keyword):
    list_of_articles=[]
    for article in keyword:
        if 'Nigeria' or 'nigeria' in country:
            list_of_articles.append(article)
            return list_of_articles

country = result

print(articles(country))



df = pd.DataFrame(country)
print(df)


df_country= df.to_csv('Nigeria_2025.csv', index=False)
print('csv successfully created')

df_nigeria= pd.read_csv('Nigeria_2025.csv')
print(df_nigeria)



