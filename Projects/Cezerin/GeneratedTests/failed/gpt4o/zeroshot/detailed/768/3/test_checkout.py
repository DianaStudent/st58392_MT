from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on product category
        category_a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a.click()

        # Step 3: Select the first product
        product_a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Verify "GO TO CHECKOUT" button presence
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertIsNotNone(go_to_checkout_button)
        
        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form
        email_input.send_keys("mail@mail.com")

        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, ".shipping-methods input[type='radio']")
        shipping_method.click()

        payment_method = driver.find_element(By.CSS_SELECTOR, ".payment-methods input[type='radio']")
        payment_method.click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap button[type='submit']")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        place_order_button.click()

        # Step 13: Wait for confirmation page and check for "Thanks for your order!"
        confirmation_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        self.assertIn("Thanks for your order!", confirmation_text.text)

if __name__ == "__main__":
    unittest.main()