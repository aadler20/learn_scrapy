import pandas as pd
import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
headers = {'User-Agent': user_agent}

url = 'https://www.worldometers.info/world-population/'
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read()
df_pop = pd.read_html(html)

for i in range(len(df_pop)):
    print(df_pop[i].head())
    df_pop[i].to_csv('result/df_pop_{}.csv'.format(i))

url = 'http://wdi.worldbank.org/table/2.1'
request = urllib.request.Request(url=url, headers=headers)
html = urllib.request.urlopen(request).read()
df = pd.read_html(html)
print(f'Total tables: {len(df)}')
for i in range(len(df)):
    print(df[i].head())
