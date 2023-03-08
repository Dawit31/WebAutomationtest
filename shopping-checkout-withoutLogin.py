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

    def test_shopping_checkout_noLogin(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-3']/div/div/div[3]/div[2]/div[@class='product-item']//input[@value='Add to cart']").click()
        driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_RecipientName']").send_keys("admin")
        ##driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_RecipientEmail']").send_keys("davidcancel30@gmail.com")
        ##driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_SenderName']").send_keys("Test")
        ##driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_SenderEmail']").send_keys("davidcancel30@gmail.com")
        ##driver.find_element(By.XPATH,"/html//textarea[@id='giftcard_2_Message']").send_keys("Beli ini 1 pcs aja yaaa buat coba cobaaa ini dicoba okeokeeeeeee")
        ##driver.find_element(By.XPATH,"/html//input[@id='add-to-cart-button-2']").click()
        ##data = driver.find_element(By.XPATH,"/html//div[@id='bar-notification']").text
        ##self.assertIn("The product has been added to your shopping cart",data)
        ##driver.find_element(By.XPATH,"//li[@id='topcartlink']//span[@class='cart-label']").click()
        time.sleep(10)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()