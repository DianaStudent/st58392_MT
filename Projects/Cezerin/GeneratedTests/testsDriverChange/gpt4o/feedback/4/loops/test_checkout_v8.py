import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        driver.get("http://localhost:3000/")

        # Step 2: Click on product category
        category_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        if not category_link:
            self.fail("Category link not found.")
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        if not product_link:
            self.fail("Product link not found.")
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.button-addtocart .button'))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-button'))
        )
        if not cart_button:
            self.fail("Cart button not found.")
        cart_button.click()

        # Step 6: Verify "GO TO CHECKOUT" button
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]'))
        )
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found.")
        go_to_checkout_button.click()

        # Step 8: Wait for checkout form to appear
        wait.until(EC.presence_of_element_located((By.ID, 'customer.email')))

        # Step 9: Fill required checkout fields
        email_input = driver.find_element(By.ID, "customer.email")
        if not email_input:
            self.fail("Email input not found.")
        email_input.send_keys("mail@mail.com")

        phone_input = driver.find_element(By.ID, "customer.mobile")
        if not phone_input:
            self.fail("Phone input not found.")
        phone_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        if not state_input:
            self.fail("State input not found.")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        if not city_input:
            self.fail("City input not found.")
        city_input.send_keys("Riga")

        # Step 10: Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, 'input[name="shipping_method_id"]')
        if not shipping_method:
            self.fail("Shipping method not found.")
        shipping_method.click()

        payment_method = driver.find_element(By.CSS_SELECTOR, 'input[name="payment_method_id"]')
        if not payment_method:
            self.fail("Payment method not found.")
        payment_method.click()

        # Step 11: Click "Next"
        next_button = driver.find_element(By.CSS_SELECTOR, '.checkout-button-wrap .button')
        if not next_button:
            self.fail("Next button not found.")
        next_button.click()

        # Step 12: Click "Place Order"
        place_order_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-step:nth-child(2) button[type="submit"]'))
        )
        if not place_order_button:
            self.fail("Place Order button not found.")
        place_order_button.click()

        # Step 13: Confirm the success message
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-success-title'))
        )
        if not success_message or "Thanks for your order!" not in success_message.text:
            self.fail("Success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()