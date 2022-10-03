import time

from selenium import webdriver


class Firefox():

    def firefox_launch(self):
        driver = webdriver.Firefox(executable_path="C:\\Driver\\geckodriver-v0.31.0-win64\\geckodriver.exe")

        time.sleep(5)
        driver.close()


test_object = Firefox()
test_object.firefox_launch()