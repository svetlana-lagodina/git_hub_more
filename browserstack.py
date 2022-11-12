# https://www.browserstack.com/docs/automate/selenium/getting-started/python#run-your-first-test

class windows_10_1920_1080_chrome(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = KEY.my_key or 'https://bsuser_n8mSb9:BYG6rRj8oKMRw5uxE7Xb@hub-cloud.browserstack.com/wd/hub'
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):


    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')

    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')

    driver.quit() #after every test