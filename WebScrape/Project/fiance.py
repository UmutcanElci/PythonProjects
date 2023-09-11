from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Malat\\Desktop\\chromedriver-win64\\chromedriver.exe")

driver.get('https://www.google.com/finance/quote/ZOREN:IST?hl=tr')

wait = WebDriverWait(driver, 10)

try:
    while True:
        
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="YMlKec fxKbKc"]')))
        
        fiyat = element.text
        print(f'Fiyat: {fiyat}')
        
        
        
        time.sleep(60)
        driver.refresh()

except KeyboardInterrupt:
    driver.quit()
