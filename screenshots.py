driver.get_screenshot_as_file('logo_loading_error.png')
driver.save_screenshot('logo_loading_error.png')
(работают одинаково, во втором можно сначала прописать путь)
driver.save_screenshot('C:\AllureReports\logo_loading_error.png')

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

# TakeElementScreenshot v
ele.screenshot('./image.png')