from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Malat\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(options=options)
url = "https://www.google.com/finance/portfolio/watchlist?hl=tr"
driver.get(url)
wait = WebDriverWait(driver, 10)


firma_elements = driver.find_elements(By.XPATH, '//div[@class="rBKq4"]//div[@class="COaKTb"]')
firmalar = []

for element in firma_elements:
    firma = element.text
    firmalar.append(firma)

firmalar_yanyana = ' - '.join(firmalar)
print(f'Firmalar: {firmalar_yanyana}')

try:
    while True:
        fiyat_elements = driver.find_elements(By.XPATH, '//div[@class="rBKq4"]//div[@class="YMlKec"]')
        fiyatlar = []

        for element in fiyat_elements:
            fiyat = element.text
            fiyatlar.append(fiyat)

        fiyatlar_yanyana = ' - '.join(fiyatlar)

        print(f'Fiyatlar: {fiyatlar_yanyana}')

        time.sleep(60)
        driver.refresh()

except KeyboardInterrupt:
    driver.quit()
