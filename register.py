import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:/WebDriver/chromedriver.exe")

    def test_success_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/register']").click()
        driver.find_element(By.CSS_SELECTOR)
        time.sleep(10)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()