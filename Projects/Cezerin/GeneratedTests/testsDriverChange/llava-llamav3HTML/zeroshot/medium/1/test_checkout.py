import unittest
from selenium import webdriver
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class TestOrderCreation(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()
    
    def test_order_creation(self):
        # Open home page
        self.driver.get('http://localhost:3000/')
        
        # Click on product category
        category_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("Category A")]'))))
        category_link.click()
        
        # Select the first product
        product_first = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("Product A")]'))))
        product_first.click()
        
        # Click the cart icon/bottom to open the mini-cart
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("cart")))]'))
        cart_icon.click()
        
        # Add a product to the cart
        add_product_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("Add to cart"))]}')))
        add_product_button.click()
        
        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("GO TO CHECKOUT")]))))
        if not go_to_checkout_button:
            self.fail('Failed to find GO TO CHECKOUT Button')
        
        # Click the cart icon/bottom to open the mini-cart
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("cart")))]')))
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("cart"))]}')))
        cart_icon.click()
        
        # Fill required checkout fields
        email_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("email"))]}')))
        phone_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("phone"))]}')))
        shipping_address_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("shipping_address"))]}')))
        payment_method_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("payment_method"))]}')))
        
        # Select a shipping and payment method
        select_email = Select(email_input)
        select_phone = Select(phone_input)
        select_address = Select(shipping_address_input)
        select_payment_method = Select(payment_method_input)
        email = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("email"))]}')))
        
        for option in select_email.all_by_text('test@example.com'):
            select_email.select_by_value(option)
        for option in select_phone.all_by_text('12345678901'):
            select_phone.select_by_value(option)
        for option in select_address.all_by_text('1234 Main St, Anytown USA 12345'):
            select_address.select_by_value(option)
        for option in select_payment_method.all_by_text('PayPal'):
            select_payment_method.select_by_value(option)
        
        # Click "Next" and then "Place Order"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("NEXT"))]}')))
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("PLACE ORDER")]))))
        place_order_button.click()
        
        # Confirm that the final success page contains the message: "Thanks for your order!"
        success_page = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text("Thanks for your order!")]))))
        if not success_page:
            self.fail('Failed to find Success Page')
    
if __name__ == '__main__':
    unittest.main()