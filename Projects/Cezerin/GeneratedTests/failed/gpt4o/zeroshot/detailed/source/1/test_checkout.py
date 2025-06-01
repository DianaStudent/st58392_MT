from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Open home page
        try:
            driver.get("http://localhost:3000/")
        except Exception as e:
            self.fail(f"Cannot open homepage: {str(e)}")

        # Click on product category
        try:
            category_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))
            )
            category_link.click()
        except TimeoutException:
            self.fail("Category link not found")

        # Select the first product
        try:
            product_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            product_link.click()
        except TimeoutException:
            self.fail("Product link not found")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button"))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Add to cart button not found")

        # Click the cart icon/button to open the shopping bag
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img"))
            )
            cart_button.click()
        except TimeoutException:
            self.fail("Cart button not found")

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']"))
            )
        except TimeoutException:
            self.fail("GO TO CHECKOUT button not found in cart")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Wait for the checkout form to appear
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
        except TimeoutException:
            self.fail("Checkout form not found")

        # Fill out the checkout form fields
        email_field.send_keys("mail@mail.com")
        phone_field = driver.find_element(By.ID, "customer.mobile")
        phone_field.send_keys("12345678")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")
        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        shipping_method.click()
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        payment_method.click()

        # Click the "Next" button
        try:
            next_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))
            )
            next_button.click()
        except TimeoutException:
            self.fail("Next button not found")

        # Click the "Place Order" button
        try:
            place_order_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.is-primary"))
            )
            place_order_button.click()
        except TimeoutException:
            self.fail("Place Order button not found")

        # Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        try:
            confirmation_text = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]"))
            )
            self.assertTrue("Thanks for your order!" in confirmation_text.text)
        except TimeoutException:
            self.fail("Order confirmation message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()