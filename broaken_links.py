from requests.exceptions import InvalidSchema, MissingSchema
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://qasvus.wixsite.com/ca-marketing')
links = driver.find_elements(By.CSS_SELECTOR, "a")

for link in links:
    try:
        r = requests.get(link.get_attribute('href'))
        print (r)
        time.sleep(5)
        if r.status_code == 200:
            print(link.get_attribute('href'), " ok")
        else:
            print(link.get_attribute('href'), r)
    except StaleElementReferenceException:
        print("impossible to get response")
    except (InvalidSchema, MissingSchema):
        print(link.get_attribute('href'), " impossible to get response")
