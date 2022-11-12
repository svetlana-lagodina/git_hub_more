# Perform click-and-hold action on the element
webdriver.ActionChains(driver).click_and_hold("element").perform()
# Performs release event
webdriver.ActionChains(driver).release().perform()


# Perform right-click action on the element
webdriver.ActionChains(driver).context_click("element").perform()


# Perform double-click action on the element
webdriver.ActionChains(driver).double_click("element").perform()


#DRAG AND DROP
# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as source element
targetEle = driver.find_element(By.ID, "droppable")
# Performs drag and drop action of sourceEle onto the targetEle
webdriver.ActionChains(driver).drag_and_drop(sourceEle, targetEle).perform()


# Performs mouse move action onto the element
webdriver.ActionChains(driver).move_to_element(gmailLink).perform()