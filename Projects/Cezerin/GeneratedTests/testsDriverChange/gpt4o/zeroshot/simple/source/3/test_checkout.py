import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_checkout_process(self):
        driver = self.driver

        # Navigate to Category A
        category_a_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
        category_a_link.click()

        # Open Product A page
        product_a_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
        product_a_link.click()

        # Click "Add to cart"
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()

        # Wait for "GO TO CHECKOUT" button and click
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "GO TO CHECKOUT")))
        go_to_checkout_button.click()

        # Fill in the checkout form
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")
        
        mobile_input = self.driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")
        
        state_input = self.driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")
        
        city_input = self.driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Select shipping method
        shipping_method_radio = self.driver.find_element(By.NAME, "shipping_method_id")
        shipping_method_radio.click()

        # Select payment method
        payment_method_radio = self.driver.find_element(By.NAME, "payment_method_id")
        payment_method_radio.click()

        # Click "Next" button
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap .button")))
        next_button.click()

        # Place order
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-step:nth-of-type(2) .checkout-button-wrap .button")))
        place_order_button.click()
        
        # Confirm order placed
        success_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()