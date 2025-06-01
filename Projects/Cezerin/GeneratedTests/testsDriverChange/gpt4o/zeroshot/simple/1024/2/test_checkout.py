import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A
        category_a_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_a_link.click()

        # Select Product A
        product_a_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        product_a_link.click()

        # Add to Cart
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
        )
        add_to_cart_button.click()

        # Open Cart
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button img[title='cart']"))
        )
        cart_button.click()

        # Go to Checkout
        go_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Go to checkout']"))
        )
        go_to_checkout_button.click()

        # Fill Checkout Details
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        email_input.send_keys("mail@mail.com")

        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")
        
        # Select Shipping Method
        shipping_method_radio = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        shipping_method_radio.click()
        
        # Select Payment Method
        payment_method_radio = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        payment_method_radio.click()

        # Proceed to Shipping
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        # Place Order
        place_order_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
        )
        place_order_button.click()

        # Verify Order Success
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertIsNotNone(success_message, "Order success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()