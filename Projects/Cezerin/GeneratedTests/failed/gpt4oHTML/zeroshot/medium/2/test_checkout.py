from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')  # Replace with the actual URL

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open home page (already opened in setUp)
        
        # Step 2: Click on product category
        category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()
        
        # Step 3: Select the first product
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()
        
        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()
        
        # Step 5: Click the cart icon/button to open the shopping bag
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_icon.click()
        
        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']")))
        
        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()
        
        # Step 8: Fill required checkout fields
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")
        
        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")
        
        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        
        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")
        
        # Step 9: Select a shipping and payment method
        shipping_method_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method input[value='67ca982ef38a654a7c2c1a69']")))
        shipping_method_radio.click()
        
        payment_method_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method input[value='67ca982ef38a654a7c2c1a6a']")))
        payment_method_radio.click()
        
        # Step 10: Click "Next" and then "Place Order" to complete the process
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap .is-primary")))
        next_button.click()
        
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.is-primary")))
        place_order_button.click()
        
        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        self.assertIn("Thanks for your order!", success_message.text)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()