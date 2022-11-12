# SUB MENU
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav # submenu1")
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()


#object of ActionChains
a = ActionChains(driver)
#identify element
m = driver.find_element(By.LINK_TEXT, "Enabled")
#hover over element
a.move_to_element(m).perform()
#identify sub menu element
n = driver.find_element(By.LINK_TEXT, "Back to JQuery UI")
# hover over element and click
a.move_to_element(n).click().perform()