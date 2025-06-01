from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.select_list import Select

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
    
    def tearDown(self):
        self.driver.quit()
    
    def test_checkout(self):
        # Step 1: Open the home page
        self.driver.get("http://localhost/")
        
        # Step 2: Log in using the provided credentials
        email_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name('email'))
        )
        email_field.send_keys('test22@user.com')
        password_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name('password'))
        )
        password_field.send_keys('test**11')
        login_button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_tag_name('button'))
        )
        self.driver.execute_script('arguments[0].click();', login_button)
        
        # Step 3: Add product to the cart
        product_page_url = WebDriverWait(self.driver, 20).until(
            lambda x: x.current_url()
        )
        self.driver.get(product_page_url)
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name('add-to-cart-button')
        )
        self.driver.execute_script('arguments[0].click();', add_to_cart_button)
        
        # Step 4: Open the cart page
        cart_page_url = WebDriverWait(self.driver, 20).until(
            lambda x: x.current_url()
        )
        self.driver.get(cart_page_url)
        proceed_button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name('proceed-to-checkout-button')
        )
        self.driver.execute_script('arguments[0].click();', proceed_button)
        
        # Step 5: Fill in the billing form
        address_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name('address')
        )
        self.address = '123 Main St'
        self.address_field = Select(self.driver.find_element_by_tag_name('select'))
        for option in self.address_field.options:
            if option.text == 'Main':
                self.address_field.select_by_visible_text('Main')
                break
        address_field.send_keys(self.address)
        
        # Step 6: Accept terms and proceed.