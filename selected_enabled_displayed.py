# Get boolean value for is element display
is_button_visible = driver.find_element(By.CSS_SELECTOR, "[name='login']").is_displayed()

    # Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'btnK').is_enabled()

    # Returns true if element is checked else returns false
value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()