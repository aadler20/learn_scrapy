from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import numpy as np

driver = webdriver.Chrome()
driver.set_window_size(1080, 800)
driver.get('http://data.stats.gov.cn/easyquery.htm?cn=E0101')
sleep(2)

locator = (By.XPATH, "//div[@class='mr-content']")
WebDriverWait(driver, 20, 2).until(
    EC.presence_of_element_located(locator))
sleep(3)

driver.find_element(
    By.XPATH, '//a[@id="{}"]'.format('treeZhiBiao_4_a')).click()
sleep(10)

driver.find_element(
    By.XPATH, '//a[@id="{}"]'.format('treeZhiBiao_10_a')).click()
sleep(10)

js = "var q=document.documentElement.scrollTop=800"
driver.execute_script(js)
sleep(10)

driver.find_element(
    By.XPATH, '//a[@id="{}"]'.format('treeZhiBiao_33_a')).click()
sleep(10)

driver.find_element(
    By.XPATH, '//div[@id="mySelect_sj"]/div[@class="dtHtml"]/div[@class="dtHead"]').click()

driver.find_element(
    By.XPATH,
    '//div[@id="mySelect_sj"]/div[@class="dtHtml"]/div[@class="dtBody"]/div[@class="dtFoot"]/input[@class="dtText"]').send_keys(
    "2005-2019")
sleep(10)

driver.find_element(By.XPATH, '//div[@class="dtTextBtn"]').click()
sleep(10)
driver.find_element(
    By.XPATH, '//div[@id="mySelect_reg"]/div[@class="dtHtml"]/div[@class="dtHead"]').click()

driver.find_element(
    By.XPATH,
    '//div[@id="mySelect_reg"]/div[@class="dtHtml"]/div[@class="dtBody"]/div[@class="dtList"]/ul/li[@code="{}"]'.format(
        "130000")).click()

sleep(10)

value = driver.find_elements(By.XPATH, '//*[@id="table_main"]/tbody/tr[2]/td')
month = driver.find_elements(By.XPATH, '//*[@id="main-container"]/div[2]/div[2]/div[2]/div/div[2]/table/thead/tr/th')

a = []
b = []

for i in value:
    a.append(i.text)
for j in month:
    b.append(j.text)

a[0] = a[0].replace("\n", "")
for i in range(len(a)):
    if i == 0:
        continue
    if i == 178:
        a[i] = a[i - 1]
    if i == 1:
        a[i] = float(a[i + 11])

    if a[i] == "":

        a[i] = (float(a[i - 1]) + float(a[i + 11])) / 2

    else:
        a[i] = float(a[i])
# 将b添加月份信息
for i in range(15):
    if i == 0:
        for j in range(3):
            b[8 + j] = str(2019 - i) + "年" + str(3 - j) + "月"  # 只到19年3月份
    else:
        for p in range(12):
            b[i * 12 + p - 1] = str(2019 - i) + "年" + str(12 - p) + "月"  # i=1p=0时b11=2018.12

for i in range(len(b)):
    if i == 0:
        continue
    b[i] = b[i].replace("年", '-')
    b[i] = b[i].replace("月", "")

dataframe = pd.DataFrame(a, b)
dataframe.to_csv("test.csv", index=True, encoding="utf-8-sig")

print("完成")