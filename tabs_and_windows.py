   # Opens a new tab and switches to new tab, Selenium 4
driver.switch_to.new_window('tab')

    # Opens a new window and switches to new window, Selenium 4
driver.switch_to.new_window('window')

    #Close the tab or window
driver.close()

    #Switch back to the old tab or window
driver.switch_to.window(original_window)


original_window = driver.current_window_handle
driver.switch_to.new_window('window' or 'tab')
driver.get("https://www.selenium.dev/documentation/webdriver/browser/windows/#windows-and-tabs")
driver.switch_to.window(original_window)

driver.switch_to.new_window("tab")
driver.switch_to.new_window("window")
driver.get("")
driver.switch_to.window(original_window)

driver.switch_to.frame("")
driver.switch_to.default_content()

time.sleep(3)
driver.implicitly_wait(3)
wait=WebDriverWait(driver, 3)

wait.until(EC.element_to_be_clickable((By.XPATH, "")))
wait.until(EC.visibility_of_element_located(By.XPATH, ""))

class ChromeSsearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    def test_chrome(self):
        driver=self.driver
        driver.get()
        driver.title
        driver.maximize_window()
        driver.minimize_window()
        driver.set_window_size(1024, 768)

        time.sleep(3)
        driver.implicitly_wait(3)
        wait=WebDriverWait(driver, 3)

        driver.switch_to.frame(iframe)
        driver.switch_to.defaul_content()

        driver.open_new_window("tab")
        driver.get("")

        assert len(driver.window_handles)==1
        original_window=driver.current_window_handle

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle!=original_window:
                driver.switch_to_window(window_handle)
                break
        driver.switch_to_window(original_window)

        a=ActionChains(driver)
        a.move_to_element().perform()
        a.key_down(Keys.SHIFT).send_keys_to_element(search, "dddd").key_up(Keys.Shift).send_keys("ddd").perform()
        a.key_down(Keys.CONTROL).send_keys("a").perform()
        фюсщтеучеюсдшсл()юзукащкь()
        a.double_cleck().perform
        a.click_and_hold().perform()
        a.drug_and_drop()

