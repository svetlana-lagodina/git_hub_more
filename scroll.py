#Scroll to element
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")
element = driver.find_element(By.ID, "closepopup")

ActionChains(driver).scroll(0, 0, 0, 0, origin=element).perform()
time.sleep(5)

driver.quit()

#скрипт с курса
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
