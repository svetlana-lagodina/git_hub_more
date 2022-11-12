    # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

    # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()

    # Send Keys
search = driver.find_element(By.NAME, "q")
action = webdriver.ActionChains(driver)
action.move_to_element(search).click().send_keys("send_keys", Keys.ENTER).perform()