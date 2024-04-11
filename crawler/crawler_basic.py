# Import the requests library
import requests

# Define the URL of the website to scrape
URL = "https://www.dufe.edu.cn/"
# Send a GET request to the specified URL and store the response in 'resp'
resp = requests.get(URL)
# Print the HTTP status code of the response to check if the request was successful
print("sent request to {0} and got Status Code: {1}".format(URL, resp.status_code))

URL = "https://www.dufe.edu.cn/robots.txt"
resp = requests.get(URL)
print("sent request to {0} and got Status Code: {1}".format(URL, resp.status_code))

#user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
#headers = {'User-Agent': user_agent}
URL = "https://www.douban.com/robots.txt"
resp = requests.get(URL) # 418 I'm a teapot
#resp = requests.get(URL, headers=headers)
print("sent request to {0} and got Status Code: {1}".format(URL, resp.status_code))
print("\nResponse Content:")
print(resp.text)

URL = "https://www.dufe.edu.cn/"
resp = requests.get(URL)
print("sent request to {0} and got Status Code: {1}".format(URL, resp.status_code))
with open('result/dufe.txt', 'w', encoding='utf-8') as f:
    f.write(resp.text)

URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(URL)
# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    data = response.json()
    # Print the parsed data (ISS location details)
    print("ISS Location Data:")
    print(data)
else:
    print(
        f"Error: Failed to retrieve data. Status code: {response.status_code}")

image_url = "https://www.dufe.edu.cn/css/dufe/img/global/logo.png"
output_filename = "result/dufe_logo.png"
response = requests.get(image_url)
if response.status_code == 200:
    with open(output_filename, "wb") as file:
        file.write(response.content)
    print(f"Image downloaded successfully as {output_filename}")
else:
    print("Failed to download the image.")

import pandas as pd

url = "https://www.boc.cn/sourcedb/whpj/"
extracted_tables = pd.read_html(url)

if extracted_tables:
    for idx, table in enumerate(extracted_tables, 1):
        if table.shape[0] > 2:
            print(f"Table {idx}:")
            print(table)
            table.to_csv("result/table_{}.csv".format(idx), index = False)
            print("-" * 50)
else:
    print("No tables found on the webpage.")
