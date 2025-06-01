from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_and_checkout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open home page
        # No specific actions needed as it's already opened

        # Click on product category
        category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Select the first product
        product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Open the mini-cart explicitly
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Check for "GO TO CHECKOUT" button in the mini-cart
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "a[href='/checkout']"
        )))

        if not go_to_checkout_button.is_displayed():
            self.fail("GO TO CHECKOUT button is not displayed in the mini-cart")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")

        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Select a shipping method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        shipping_method.click()

        # Select a payment method
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        payment_method.click()

        # Click "Next"
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.button.is-primary")
        next_button.click()

        # Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.button.is-primary")))
        place_order_button.click()

        # Confirm the success message
        success_message = wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h1.checkout-success-title"), 
            "Thanks for your order!"
        ))

        if not success_message:
            self.fail("Order success message not found")

if __name__ == "__main__":
    unittest.main()