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
        if not category_link:
            self.fail("Category link not found.")
        category_link.click()

        # Step 2: Select the first product
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        if not first_product:
            self.fail("Product link not found.")
        first_product.click()

        # Step 3: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        if not add_to_cart_button or not add_to_cart_button.is_enabled():
            self.fail("Add to cart button not found or not clickable.")
        add_to_cart_button.click()

        # Step 4: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button img[title='cart']")))
        if not cart_button:
            self.fail("Cart button not found.")
        cart_button.click()

        # Step 5: Verify the "GO TO CHECKOUT" button and click it
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-cart-open .button.is-primary")))
        if not go_to_checkout_button or not go_to_checkout_button.text.strip():
            self.fail("GO TO CHECKOUT button not found or empty.")
        go_to_checkout_button.click()

        # Step 6: Fill out the checkout form fields
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        if not email_input:
            self.fail("Email input not found.")
        email_input.send_keys("mail@mail.com")

        mobile_input = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        if not mobile_input:
            self.fail("Mobile input not found.")
        mobile_input.send_keys("12345678")

        state_input = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        if not state_input:
            self.fail("State input not found.")
        state_input.send_keys("Riga")

        city_input = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        if not city_input:
            self.fail("City input not found.")
        city_input.send_keys("Riga")

        # Step 7: Select a shipping and payment method
        shipping_method = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-methods input[type='radio']")))
        if not shipping_method or not shipping_method.is_enabled():
            self.fail("Shipping method not selectable.")
        shipping_method.click()
        
        payment_method = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-methods input[type='radio']")))
        if not payment_method or not payment_method.is_enabled():
            self.fail("Payment method not selectable.")
        payment_method.click()

        # Step 8: Click the "Next" button
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap .checkout-button")))
        if not next_button or not next_button.is_enabled():
            self.fail("Next button not clickable.")
        next_button.click()

        # Step 9: Click the "Place Order" button
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-step button.is-primary[type='submit']")))
        if not place_order_button or not place_order_button.is_enabled():
            self.fail("Place order button not clickable.")
        place_order_button.click()

        # Step 10: Check for confirmation message
        success_title = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        if not success_title or "Thanks for your order!" not in success_title.text:
            self.fail("Order confirmation message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()