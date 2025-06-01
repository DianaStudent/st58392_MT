import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open home page
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logo-image")))

        # Step 2: Click on product category
        category_a_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))
        )
        category_a_link.click()

        # Step 3: Select the first product
        product_a_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        product_a_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button"))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        cart_button.click()
        
        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']"))
        )
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not present")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form fields
        email_input = driver.find_element(By.ID, "customer.email")
        email_input.clear()
        email_input.send_keys("mail@mail.com")

        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.clear()
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.clear()
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.clear()
        city_input.send_keys("Riga")

        # Step 10: Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        shipping_method.click()
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        payment_method.click()

        # Step 11: Click "Next" button
        next_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap .checkout-button.is-primary"))
        )
        next_button.click()

        # Step 12: Click "Place Order" button
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap button.is-primary"))
        )
        place_order_button.click()

        # Step 13: Confirm that the success page contains the message: "Thanks for your order!"
        order_success_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "checkout-success-title"))
        )
        self.assertIn("Thanks for your order!", order_success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()