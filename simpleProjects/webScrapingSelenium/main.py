from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

link=sys.argv
print(link[1])
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='/home/kaplan/PycharmProjects/webScra/chromedriver', options=chrome_options)

url =link[1]#'https://www.sahibinden.com/motosiklet?a269_min=2010&a107364=1211989&a267=39954&sorting=price_asc' #
driver.get(url)
driver.wait = WebDriverWait(driver, 5)
try:
    sayfaSayisi = driver.find_elements_by_class_name("mbdef")[0]
    sayfaSayisiVal = sayfaSayisi.text
    sayfaSayisiVal = int(sayfaSayisiVal.split()[1])
except IndexError:
    sayfaSayisiVal = 1

fiyatlar = []
print(url.find('?'))
if url.find('?') == -1:
    paging = "?pagingOffset="
else:
    paging = "&pagingOffset="

try:
    for sayfa in tqdm(range(sayfaSayisiVal)):

        nurl = url + paging + str(sayfa * 20)
        driver.get(nurl)
        driver.wait = WebDriverWait(driver, 5)
        araclar = driver.find_elements_by_class_name("searchResultsItem")
        for i in araclar:
            aracFiyatlari = i.find_elements_by_class_name("searchResultsPriceValue")
            if aracFiyatlari.__len__() == 1:
                fiyatlar.append(float(aracFiyatlari[0].text.split()[0]))
except:
    pass
driver.wait = WebDriverWait(driver, 5)
driver.close()

x = np.arange(0, len(fiyatlar))
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, fiyatlar, rcond=None)[0]
plt.plot(x, m * x + c, 'r', label='Fitted line')
plt.scatter(x=x, y=fiyatlar)
print(x.max())
plt.title(url + "\nToplam:" + str(fiyatlar.__len__()))
plt.show()

# driver.save_screenshot("test.png")
