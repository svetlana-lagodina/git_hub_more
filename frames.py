   # Store iframe web element
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

    # switch to selected iframe
driver.switch_to.frame(iframe)

    # Switch frame by id
driver.switch_to.frame('buttonframe')

    # switching to second iframe based on index
iframe = driver.find_elements_by_tag_name('iframe')[1]

    # switch back to default content
driver.switch_to.default_content()