import time
import unittest
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import WebDriverException as WDE
from webdriver_manager.chrome import ChromeDriverManager


class windows_10_chrome(unittest.TestCase):

    # setup function
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # check if social media icons are clickable
    def test_create_account(self):
        driver = self.driver
        driver.get("https://www.flirt4free.com/")
        self.driver.maximize_window()

        # random delay function
        def delay_1_5():
            time.sleep(random.randint(1, 5))

        # check the title of the page
        assert "Flirt4Free" in driver.title
        print("The title of the page is:", driver.title)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # set up faker library
        f = Faker()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='register-line-2'][contains(.,'CREDITS!')]"))).click()
        self.assertTrue(driver.find_element(By.ID, "registration_form").is_displayed())
        print ("Registration form is displayed")

        try:
            driver.find_element(By.ID, "cemail").send_keys(f.ascii_email())
            print ("The email was entered successfully")
        except WDE:
            print ("Something is wrong with email")

        try:
            driver.find_element(By.ID, "nick_name").send_keys(f.first_name()+"_"+f.last_name())
            print ("The nickname was entered successfully")
        except WDE:
            print ("Something is wrong with nickname")

        try:
            driver.find_element(By.ID, "new_password").send_keys(random.randint(8))
            print ("The nickname was entered successfully")
        except WDE:
            print ("Something is wrong with nickname")


