import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
##from webdrivermanager import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        ##self.browser = webdriver.Chrome("C:/WebDriver/chromedriver.exe")
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/register']").click()
        driver.find_element(By.XPATH,"/html//input[@id='gender-male']").click()
        driver.find_element(By.XPATH,"/html//input[@id='FirstName']").send_keys("Dawit")
        driver.find_element(By.XPATH,"/html//input[@id='LastName']").send_keys("Test")
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("davidcancel03@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("Test123#")
        driver.find_element(By.XPATH,"/html//input[@id='ConfirmPassword']").send_keys("Test123#")
        driver.find_element(By.XPATH,"/html//input[@id='register-button']").click()
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']//input[@value='Continue']").click()
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/logout']").click()
        time.sleep(10)

    def test_b_fail_empthy_firstname(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/register']").click()
        driver.find_element(By.XPATH,"/html//input[@id='FirstName']").send_keys("")
        driver.find_element(By.XPATH,"/html//input[@id='LastName']").send_keys("Test")
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("oketest12@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("Oke1234")
        driver.find_element(By.XPATH,"/html//input[@id='ConfirmPassword']").send_keys("Oke1234")
        driver.find_element(By.XPATH,"/html//input[@id='register-button']").click()
        data = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .form-fields > div:nth-of-type(2) > .field-validation-error > span").text
        self.assertIn("First name is required.",data)
        time.sleep(10)

    def test_c_fail_empthy_lastname(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/register']").click()
        driver.find_element(By.XPATH,"/html//input[@id='FirstName']").send_keys("Dawit")
        driver.find_element(By.XPATH,"/html//input[@id='LastName']").send_keys("")
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("oketest12@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("Oke1234")
        driver.find_element(By.XPATH,"/html//input[@id='ConfirmPassword']").send_keys("Oke1234")
        driver.find_element(By.XPATH,"/html//input[@id='register-button']").click()
        data = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > .field-validation-error > span").text
        self.assertIn("Last name is required.",data)
        ##data = driver.find_element(By.CSS_SELECTOR,"field-validation-error").text
        ##self.assertIn("Last name is required.")
        ##data = driver.find_element(By.CSS_SELECTOR,"field-validation-error").text
        ##self.assertIn("Email is required.")
        ##data = driver.find_element(By.CSS_SELECTOR,"field-validation-error").text
        ##self.assertIn("Password is required.")
        ##data = driver.find_element(By.CSS_SELECTOR,"field-validation-error").text
        ##self.assertIn("Password is required.")
        time.sleep(10)
    def test_d_fail_existing_data(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']//div[@class='header-links']/ul//a[@href='/register']").click()
        driver.find_element(By.XPATH,"/html//input[@id='FirstName']").send_keys("Dawit")
        driver.find_element(By.XPATH,"/html//input[@id='LastName']").send_keys("Test")
        driver.find_element(By.XPATH,"/html//input[@id='Email']").send_keys("davidcancel30@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='Password']").send_keys("Oke1234")
        driver.find_element(By.XPATH,"/html//input[@id='ConfirmPassword']").send_keys("Oke1234")
        driver.find_element(By.XPATH,"/html//input[@id='register-button']").click()
        data = driver.find_element(By.CSS_SELECTOR, "form[method='post'] ul > li").text
        self.assertIn("The specified email already exists",data)
        time.sleep(10)
           
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()