class ChromeSearch(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver=webdriver.Chrome(ChromeDriverManager().install())

    def test_new(self):
        driver=self.driver
        driver.get("")
        self.driver.maximize_window()

    driver=webdriver.Chrome()
    driver.get("")

    driver.set_window_size(1024, 768)

    assert "dffd" in driver.title

    time.sleep(3)

    def random_1_5():
        time.sleep(random.randint(1,5))

    driver.implicitly_wait(10)
    wait=WebDriverWait(driver, 3)
    wait.until(EC.element_to_be_clickable(By.XPATH, "//button[contains(text(), 'new')]"))
    //*[contains(text(), 'dddd')]

    original_window=driver.current_window_handle
    assert len(driver.window_handles)==1
    driver.find_element(By.XPATH, "").click()

    for window_handle in driver.window_handles:
        if window_handle!=original_window:
            driver.switch_to.window(window_handle)
            break
    driver.switch.to_window(original_window)

    iframe=driver.find_element(By.CSS_CELECTOR, "iframe")
    driver.switch_to.frame(iframe)
    driver.switch_to.original_content()

    driver.switch_to.frame("id")

    driver.find_element(By.TAG_NAME, "html").send_key(Keys.PAGE_DOWN)

    action=ActionChains(driver)
    action.move_to_element(menu).click(submenu).perform()

    ActionChains(driver).key_down(Keys.CONTROL).send_keys_to_element(poisk, "ssss", Keys.ENTER).perform()

    ActionChains(driver).context_click(element).perform()
    ActionChains(driver).double_click(element).perform()

    driver.get_screenshot_as_file("")
    driver.save_screenshot(".png")

    def tearDown(self):
        self.driver.quit()

    driver.find_element(By.TAG_NAME, "html").send_key(Keys.PAGE_DOWN)


class ChromeSearch(unittest.TestCase):

    def detUp(self):
        self.driver=webdriver.Chrome()
        self.driver=webdriver.Chrome(ChromeDriverManager(),install())

    def test(self):
        driver=self.driver
        driver.get("")
        self.driver.maximize_window()

        assert "" in driver.title

        self.driver.set_window_size(1024, 768)

        driver.implicity_wait(10)
        time.sleep(3)

        def random():
            time.sleep(random.randint(1, 5))

        orirginal_window=driver.current_window_handle
        assert len(driver.window_handles)==1
        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle!=original_window:
                driver.switch_to.window(window_handle)
                break
        driver.switch_to.window(original_window)

        action=ActionChains(driver)

        wait=WEbDriverWait(driver, 3)

        requests.head(link.get_attribute("href"))

        r.status.code()

        send_keys("nnnn", Keys.ENTER)





