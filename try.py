import unittest
import time

from selenium.webdriver import ActionChains

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_feature(self):
        driver=self.driver
        driver.get("")
        driver.maximize_window()
        assert "" in driver.title

driver=webdriver.Chrome()
driver.get("")
driver.set_window_size(1024, 768)

time.sleep(3)
driver.implicitly_wait(10)
wait=WebDriverWait(driver, 3)

def delay_1_5():
    time.sleep(random.randint(1, 5))



wait.until(EC.element_to_be_clickable((By.XPATH, "")))
wait.until(EC.visibility_of_element_located((By.NAME, "")))

iframe=driver.find_element(By.CSS_SELECTOR, "iframe")
driver.switch_to.frame(iframe)
driver.switch_to.default_content()
driver.switch_to.frame("")


original_window=driver.current_window_handle
assert len(driver.window_handles)==1
driver.find_element(By.XPATH, "")

for window_handle in driver.window_handles:
    if window_handle!=original_window:
        driver.switch_to.window(window_handle)
        break

driver.switch_to.window(original_window)

action=ActionChains(driver)
menu=driver.find_element(By.XPATH, "")
sub_menu=driver.find_element(By.XPATH, "")
action.move_to_element(menu).click(sub_menu).perform()

webdriver.ActionChains(driver).context_click("element").perform()
webdriver.ActionChains(driver).double_click("element").perform()

search=driver.find_element(By.XPATH, "")
ActionChains(driver).key_down(Keys.SHIFT).send_keys_to_element(search, "lana"+Keys.ENTER).perform()

ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "")).click().send_keys("dfdf", Keys.ENTER).perform()

webdriver.ActionChains(driver).double_click("element").perform()

driver.get_screenshot_as_file("ffff.png")
driver.save_screenshot("fsdfsd")

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)

driver.save_screenshot("")
driver.get_screenshot_as_file("dfdf")

def delay_1_5():
    time.sleep(random.randint(1, 5))


def tearDown(self):
    self.driver.quit()












