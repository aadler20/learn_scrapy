import pandas as pd
import urllib.request

url = 'http://wdi.worldbank.org/table/2.1'
html = urllib.request.urlopen(url).read()

df = pd.read_html(html)
print(df)
