import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Click on 'Category A'
        category_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a.click()

        # Step 2: Select 'Product A'
        product_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a.click()

        # Step 3: Click 'Add to cart' button
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_btn.click()

        # Step 4: Click on the cart button to open mini-cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img")))
        cart_button.click()

        # Step 5: Verify 'GO TO CHECKOUT' button is present
        go_to_checkout = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertIsNotNone(go_to_checkout, "GO TO CHECKOUT button is missing.")

        # Step 6: Click 'GO TO CHECKOUT' button
        go_to_checkout.click()

        # Step 7: Fill checkout fields
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        mobile_field.send_keys("12345678")

        state_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        state_field.send_keys("Riga")

        city_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        city_field.send_keys("Riga")

        # Step 8: Select shipping method
        shipping_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='shipping_method_id']")))
        shipping_method.click()

        # Step 9: Select payment method
        payment_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='payment_method_id']")))
        payment_method.click()

        # Step 10: Click 'Next' button
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap button")))
        next_button.click()

        # Step 11: Click 'Place Order' button
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.is-primary")))
        place_order_button.click()

        # Step 12: Confirm success page contains 'Thanks for your order!'
        success_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertIsNotNone(success_message, "Success message is missing on the final page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()