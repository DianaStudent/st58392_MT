from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Click on product category
        category_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 2: Select the first product
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        first_product.click()

        # Step 3: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()

        # Step 4: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img[title='cart']"))
        )
        cart_button.click()

        # Step 5: Verify the "GO TO CHECKOUT" button and click it
        go_to_checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mini-cart-open .button.is-primary"))
        )
        self.assertEqual(go_to_checkout_button.text.strip(), "GO TO CHECKOUT", "GO TO CHECKOUT button not found or has incorrect text.")
        go_to_checkout_button.click()

        # Step 6: Fill out the checkout form fields
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")

        mobile_input = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        mobile_input.send_keys("12345678")

        state_input = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        state_input.send_keys("Riga")

        city_input = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        city_input.send_keys("Riga")

        # Step 7: Select a shipping and payment method
        shipping_method = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-methods input[type='radio']"))
        )
        shipping_method.click()

        payment_method = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-methods input[type='radio']"))
        )
        payment_method.click()

        # Step 8: Click the "Next" button
        next_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap .checkout-button"))
        )
        next_button.click()

        # Step 9: Click the "Place Order" button
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-step button.is-primary"))
        )
        place_order_button.click()

        # Step 10: Check for confirmation message
        success_title = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        self.assertIn("Thanks for your order!", success_title.text, "Order confirmation message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()