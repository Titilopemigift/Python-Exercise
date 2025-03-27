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
    data= response.json()
    articles = data['response']['results']


def nigeria_2025():
    list_of_articles=[]
    for article in articles:
            data_list ={
                "Title": article["webTitle"],
                "URL": article["webUrl"],
                "Section_name": article["sectionName"],
                "Publication_date": article["webPublicationDate"]
            }
            list_of_articles.append(data_list)
    return list_of_articles

result = nigeria_2025()
print(result)





df = pd.DataFrame(result)
print(df)


df_country= df.to_csv('Nigeria_2025.csv', index=False)
print('csv successfully created')

df_nigeria= pd.read_csv('Nigeria_2025.csv')
print(df_nigeria)



