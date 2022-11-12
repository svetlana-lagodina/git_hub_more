# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
original_window = driver.current_window_handle

# get element
element = driver.find_element(By.ID, "Path_249")

driver.switch_to.new_window('window')
driver.get("https://www.selenium.dev/documentation/webdriver/browser/windows/#windows-and-tabs")
driver.switch_to.window(original_window)

# print width
print(element.value_of_css_property('transform'))