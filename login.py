import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
##from webdrivermanager import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/login']").click()
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("davidcancel85@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("Test123#")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//input[@value='Log in']").click()
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/logout']").click()
        time.sleep(10)

    def test_b_fail_login_empthy_data(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/login']").click()
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//input[@value='Log in']").click()
        data = driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']/div//form[@action='/login']//div[@class='validation-summary-errors']/span").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.",data)
        time.sleep(10)
    
    def test_c_empthy_username(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/login']").click()
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("Test123#")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//input[@value='Log in']").click()
        data = driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-2']//form[@action='/login']//ul/li[.='No customer account found']").text
        self.assertIn("No customer account found",data)
        time.sleep(10)
        
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()