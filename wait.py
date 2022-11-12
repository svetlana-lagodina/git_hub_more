#implicit
driver.implicitly_wait(10)


#explicit
wait = WebDriverWait(driver, 3)
wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']")))
wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'QA at Silicon Valley California')]")))


#fluent
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))


# set up random delay
def delay_1_5():
    time.sleep(random.randint(1, 5))



# time sleep
time.sleep(2)