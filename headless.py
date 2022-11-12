options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)


class ChromeSearch(unittest.TestCase):

    # Chrome headless script
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)


    # FireFox headless script
    def ff_headless(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

    # Edge headless script
    def edge_headless(self):
        options = webdriver.EdgeOptions()
        options.headless = True
        self.driver = webdriver.Edge(options=options)