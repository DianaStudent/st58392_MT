from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_flow(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click on product category
        category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 2: Select the first product
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Step 3: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 4: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Step 5: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is missing")

        # Step 6: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 7: Fill required checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        mobile_input = driver.find_element(By.ID, "customer.mobile")
        state_input = driver.find_element(By.ID, "shipping_address.state")
        city_input = driver.find_element(By.ID, "shipping_address.city")

        email_input.send_keys("test@example.com")
        mobile_input.send_keys("12345678")
        state_input.send_keys("TestState")
        city_input.send_keys("TestCity")

        # Step 8: Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        
        shipping_method.click()
        payment_method.click()

        # Step 9: Click "Next" and then "Place Order"
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.is-primary")
        next_button.click()
        
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.is-primary")))
        place_order_button.click()

        # Step 10: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIsNotNone(success_message, "Order success message is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()