import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
##from webdrivermanager import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_shopping_checkout_checkoutasGuest(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-3']/div/div/div[3]/div[2]/div[@class='product-item']//input[@value='Add to cart']").click()
        driver.get("https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_RecipientName']").send_keys("admin")
        driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_RecipientEmail']").send_keys("davidcancel30@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_SenderName']").send_keys("Test")
        driver.find_element(By.XPATH,"/html//input[@id='giftcard_2_SenderEmail']").send_keys("davidcancel30@gmail.com")
        driver.find_element(By.XPATH,"/html//textarea[@id='giftcard_2_Message']").send_keys("Beli ini 1 pcs aja yaaa buat coba cobaaa ini dicoba okeokeeeeeee")
        driver.find_element(By.XPATH,"/html//input[@id='add-to-cart-button-2']").click()
        driver.find_element(By.XPATH,"//li[@id='topcartlink']//span[@class='cart-label']").click()
        driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-1']//form[@action='/cart']/table[@class='cart']//input[@name='removefromcart']").click()
        driver.find_element(By.XPATH,"/html//input[@id='termsofservice']").click()
        driver.find_element(By.XPATH,"/html//button[@id='checkout']").click()

        ##form checkout as Guest "Billing Address"
        driver.get("https://demowebshop.tricentis.com/onepagecheckout") 
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_FirstName']").send_keys("Dawit")
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_LastName']").send_keys("Test")
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_Email']").send_keys("davidcancel30@gmail.com")
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_Company']").send_keys("Jogja")
        select = Select(driver.find_element(By.NAME,"BillingNewAddress.CountryId"))
        select.select_by_value('2')
        select = Select(driver.find_element(By.NAME,"BillingNewAddress.StateProvinceId"))
        select.select_by_value('0')
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_City']").send_keys("Jogja")
        driver.find_element(By.XPATH,"//div[@id='billing-new-address-form']/div[@class='enter-address']/div[@class='enter-address-body']//input[@name='BillingNewAddress.Address1']").send_keys("Jl Sleman")
        driver.find_element(By.XPATH,"//div[@id='billing-new-address-form']/div[@class='enter-address']/div[@class='enter-address-body']//input[@name='BillingNewAddress.Address2']").send_keys("Jl test")
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_ZipPostalCode']").send_keys("51252")
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_PhoneNumber']").send_keys("088226871392")
        driver.find_element(By.XPATH,"/html//input[@id='BillingNewAddress_FaxNumber']").send_keys("52153325")
        driver.find_element(By.XPATH,"//div[@id='billing-buttons-container']/input[@title='Continue']").click()
        time.sleep(2)

        ##form Payment Method as Guest "Payment Method"
        payment = driver.find_element(By.XPATH,"//li[@id='opc-payment_method']/div[@class='step-title']")
        hover = ActionChains(driver).move_to_element(payment)
        time.sleep(2)
        driver.find_element(By.ID,"paymentmethod_1").click()
        driver.find_element(By.CSS_SELECTOR,"div#payment-method-buttons-container > .button-1.payment-method-next-step-button").click()
       
        ##Payment Information
        Payinfo = driver.find_element(By.XPATH,"//li[@id='opc-payment_info']//h2[.='Payment information']")
        hover = ActionChains(driver).move_to_element(Payinfo)
        driver.find_element(By.ID,"checkout-payment-info-load").text
        ##driver.find_elements(By.XPATH,"//div[@id='payment-info-buttons-container']/input[@value='Continue']").
        Payconfirm = driver.find_element(By.XPATH,"//li[@id='opc-confirm_order']//h2[.='Confirm order']")
        hover = ActionChains(driver).move_to_element(Payconfirm)
        ##driver.find_element(By.CSS_SELECTOR,"div#payment-info-buttons-container > .button-1.payment-info-next-step-button").click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "payment-info-buttons-container")))
        driver.find_element(By.XPATH,"//div[@id='payment-info-buttons-container']/input[@value='Continue']").click()
        
        #confirm Order
        confirm = WebDriverWait(driver, 10)
        element = confirm.until(EC.element_to_be_clickable((By.ID, "confirm-order-buttons-container")))
        driver.find_element(By.XPATH,"//div[@id='confirm-order-buttons-container']/input[@value='Confirm']").click()
        
        #Checkout Success
        driver.get("https://demowebshop.tricentis.com/checkout/completed/")
        success = driver.find_element(By.XPATH,"//body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-wrapper-main']/div[@class='center-1']//strong[.='Your order has been successfully processed!']").text
        self.assertIn("Your order has been successfully processed!",success)
        time.sleep(10)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()