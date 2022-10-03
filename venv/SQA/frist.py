from selenium import webdriver
driver = webdriver.Chrome("C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element("username").send_keys("Admin")
driver.find_element("password").send_keys("admin123")
