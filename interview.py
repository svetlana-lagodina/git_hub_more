#do imports
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
from webdriver_manager.chrome import ChromeDriverManager

#set up browsers
driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

#set up browsers in unittest
class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # check price filter test
    def test_real_estate_firefox(self):
        driver = self.driver
        driver.get('https://us.pandora.net/')
        self.driver.maximize_window()


#customize window, get link, assert title
driver.set_window_size(1024, 768)
driver.get("")
assert "California Real Estate" in driver.title

#waits
time.sleep(2)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 3)

#find elements with different locators
driver.find_element (By.XPATH, "")


#set up wait until and expected conditions
wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'QA at Silicon Valley California')]")))

wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']")))

#frames

iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
driver.switch_to.frame(iframe)
driver.switch_to.default_content()

    # Switch frame by id
driver.switch_to.frame('buttonframe')


#window tabs handles
# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1

# Click the link which opens in a new window
driver.find_element(By.LINK_TEXT, "Register now!").click()

# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
         driver.switch_to.window(window_handle)
         break
#Switch back to the old tab or window
driver.switch_to.window(original_window)


#actionchains
# SUB MENU
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav # submenu1")
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


#keys
    # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

    # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()

    # Send Keys
search = driver.find_element(By.NAME, "q")
action = webdriver.ActionChains(driver)
action.move_to_element(search).click().send_keys("send_keys", Keys.ENTER).perform()

driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)


#screenshots
driver.get_screenshot_as_file('logo_loading_error.png')
driver.save_screenshot('logo_loading_error.png')

#scroll
ActionChains(driver).scroll(0, 0, 0, 0, origin=element).perform()


#tear down
def tearDown(self):
    self.driver.quit()


#mouse_actions
# Perform click-and-hold action on the element
ActionChains(driver).click_and_hold("element").perform()

# Performs release event
ActionChains(driver).release().perform()

# Perform right-click action on the element
ActionChains(driver).context_click("element").perform()

# Perform double-click action on the element
ActionChains(driver).double_click("element").perform()

#API
r = requests.head(link.get_attribute('href')) (<Response [200]>)
r.status_code == 200


#set up headless
#set up webdriver manager

fake=Faker()

send_keys(fake.number)

