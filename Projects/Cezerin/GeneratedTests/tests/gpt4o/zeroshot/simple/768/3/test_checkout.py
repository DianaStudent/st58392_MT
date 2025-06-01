import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000/')
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to Category A
        category_a = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Category A')))
        category_a.click()

        # Navigate to Product A page
        product_a = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Product A')))
        product_a.click()

        # Click "Add to cart"
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.button-addtocart .button')))
        add_to_cart_button.click()

        # Click on the cart button (shopping bag)
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-button')))
        cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button and click
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'GO TO CHECKOUT')))
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, 'customer.email')))
        email_input.send_keys('mail@mail.com')

        mobile_input = driver.find_element(By.ID, 'customer.mobile')
        mobile_input.send_keys('12345678')

        state_input = driver.find_element(By.ID, 'shipping_address.state')
        state_input.send_keys('Riga')

        city_input = driver.find_element(By.ID, 'shipping_address.city')
        city_input.send_keys('Riga')

        # Select Shipping method
        shipping_method_input = driver.find_element(By.NAME, 'shipping_method_id')
        shipping_method_input.click()

        # Select Payment method
        payment_method_input = driver.find_element(By.NAME, 'payment_method_id')
        payment_method_input.click()

        # Click "Next"
        next_button = driver.find_element(By.CSS_SELECTOR, '.checkout-button-wrap .button')
        next_button.click()

        # Place order
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-button-wrap .button.is-primary')))
        place_order_button.click()

        # Confirm success page
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]")))
        self.assertIsNotNone(success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()