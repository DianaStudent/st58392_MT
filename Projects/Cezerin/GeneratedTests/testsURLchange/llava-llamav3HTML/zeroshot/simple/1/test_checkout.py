import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait

class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/chromedriver.exe")
        
    def tearDown(self):
        self.driver.quit()

    def test_order_process(self):
        # Add a product to the cart
        add_product_button = self.wait_for_element_with_text("ADD TO CART", 20)
        add_product_button.click()
        
        # Wait for presence of the "GO TO CHECKOUT" button
        checkout_button = self.wait_for_element_with_text("GO TO CHECKOUT", 20)
        self.assertEqual(checkoutbutton, "You have no items in your cart.")
        
        # Fill required checkout fields (e.g. email, phone, shipping address, Shipping, payment) using values visible in html_data
        email_field = self.wait_for_element_with_text("email", 20)
        phone_field = self.wait_for_element_with_text("phone", 20)
        shipping_address_field = self.wait_for_element_with_text("shipping_address", 20)
        select_shipping_method = Select(self.wait_for_element_with_text("shipping_method", 20))
        select_payment_method = Select(self.wait_for_element_with_text("payment_method", 20))
        
        # Place the order
        place_order_button = self.wait_for_element_with_text("PLACE ORDER", 20)
        place_order_button.click()
        
        # Confirm that the final success page contains the text: "Thanks for your order!"
        final_success_page_message = self.wait_for_element_with_text("Thanks for your order!", 20)
        self.assertEqual(final_success_page_message, "Thanks for your order!")
    
if __name__ == '__main__':
    unittest.main()