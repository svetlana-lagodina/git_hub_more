from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# Open URL
driver.get("https://www.selenium.dev/")

# Setup wait for later
wait = WebDriverWait(driver, 10)

# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1

# Click the link which opens in a new window
driver.find_element(By.LINK_TEXT, "Register now!").click()

# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
         driver.switch_to.window(window_handle)
         break

# Wait for the new tab to finish loading content
wait.until(EC.title_is("SeleniumHQ Browser Automation"))


original_window=driver.current_window_handle
assert len(driver.window_handles)==1
driver.find_element(By.LINK_TEXT, "Register now!").click()
wait=WebDriverWait(driver, 3)
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
    if window_handle!=original_window:
        driver.switch_to.window(window_handle)
        break


original_window=driver.current_window_handle
assert len(driver.window_handles)==1
driver.find_element(By.XPATH).click()
for window_handle in driver.window_handles:
    if window_handle!=original_window:
        driver.switch_to.window(window_handle)
        break