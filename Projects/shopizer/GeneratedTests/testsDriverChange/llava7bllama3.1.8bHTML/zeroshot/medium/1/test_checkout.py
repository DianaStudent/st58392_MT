from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCartCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/checkout") # replace with your URL

    def test_cart_checkout(self):
        self.login()
        self.add_product_to_cart()
        self.open_cart_page()
        self.click_proceed_to_checkout()
        self.fill_billing_form()

    def login(self):
        username_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "login-email"))
        )
        username_input.send_keys("test22@user.com")
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "login-password"))
        )
        password_input.send_keys("test**11")
        self.driver.find_element_by_id('login-submit').click()

    def add_product_to_cart(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click() # replace with your product button

    def open_cart_page(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "cart-link"))
        ).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element_by_id('proceed-to-checkout').click()

    def fill_billing_form(self):
        # wait for region select to appear
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "region-id"))
        )
        
        name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "billing-name"))
        )
        name_input.send_keys("Test User")
        
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "billing-email"))
        )
        email_input.send_keys("test22@user.com")
        
        address_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "billing-address-1"))
        )
        address_input.send_keys("123 Main St")
        
        self.driver.find_element_by_id('region-id').send_keys("Ontario") # replace with your region
        phone_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "billing-phone"))
        )
        phone_input.send_keys("555-1234")
        
        self.driver.find_element_by_id('billing-province').click()
        self.driver.find_element_by_xpath("//option[@value='Ontario']").click()

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()