#pip install allure-pytest
#Add "AllureReports" folder to your Project root

import AllureReports
if __name__ == "__main__":
    unittest.main(AllureReports)

py.test --alluredir=./AllureReports ./unittest15.py
allure serve ./AllureReports


#pip install -U pytest
#pip3 install -U pytest
#pip install html-testRunner
#add folder "HtmlReports" to your project

import HtmlTestRunner
import HTMLTestRunner

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

python unittest14.py
py unittest14.py
