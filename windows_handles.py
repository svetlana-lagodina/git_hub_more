driver.find_element(By.LINK_TEXT, "link").click()

handles = driver.window_handles
size = len(handles)

for x in range(size):
  driver.switch_to.window(handles[x])
  print(driver.title)
