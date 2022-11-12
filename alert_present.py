from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# maximize with maximize_window()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify element and click()

wait = WebDriverWait(driver, 3)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='submit']"))).send_keys('\n')

print ("clicked")
# alert_is_present() expected condition wait for 5 seconds
try:
   WebDriverWait(driver, 5).until(EC.alert_is_present())
   # switch_to.alert for switching to alert and accept
   alert = driver.switch_to.alert
   alert.accept()
   print("alert Exists in page")
except TimeoutException:
   print("alert does not Exist in page")
driver.close()