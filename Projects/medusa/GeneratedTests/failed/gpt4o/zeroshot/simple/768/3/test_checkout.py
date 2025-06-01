from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MedusaCheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to store
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-store-link']")))
        store_link.click()
        
        # Add product to cart
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
        product_link.click()
        
        size_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()
        
        # Go to cart
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_link.click()
        
        # Proceed to checkout
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-checkout-button']")))
        go_to_checkout_button.click()
        
        # Fill out shipping address
        shipping_first_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='shipping_address.first_name']")))
        shipping_first_name.send_keys("user")

        shipping_last_name = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_address.last_name']")
        shipping_last_name.send_keys("test")

        shipping_address = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_address.address_1']")
        shipping_address.send_keys("street 1")

        shipping_postal_code = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_address.postal_code']")
        shipping_postal_code.send_keys("LV-1021")

        shipping_city = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_address.city']")
        shipping_city.send_keys("Riga")

        shipping_country_select = driver.find_element(By.CSS_SELECTOR, "select[name='shipping_address.country_code']")
        shipping_country_select.send_keys("Denmark")

        shipping_email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        shipping_email.send_keys("user@test.com")

        # Continue to delivery
        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Select delivery method
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']")))
        delivery_option.click()
        
        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Select payment method
        manual_payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='radio-button']")))
        manual_payment_option.click()
        
        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Place order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify order completion
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
        self.assertTrue(success_message, "Order was not placed successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()