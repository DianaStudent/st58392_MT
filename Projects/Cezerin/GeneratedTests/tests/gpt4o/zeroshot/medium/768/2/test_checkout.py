import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open home page and click on product category
        category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Select the first product
        product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Click the cart icon to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered")
        ))

        # If not found, fail the test
        if not go_to_checkout_button:
            self.fail('GO TO CHECKOUT button not found in the cart.')

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")

        mobile_input = wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        mobile_input.send_keys("12345678")

        state_input = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        state_input.send_keys("Riga")

        city_input = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        city_input.send_keys("Riga")

        # Select a shipping and payment method
        shipping_method = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='shipping_method_id']")
        ))
        shipping_method.click()

        payment_method = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='payment_method_id']")
        ))
        payment_method.click()

        # Click "Next" button
        next_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.checkout-button.is-primary")
        ))
        next_button.click()

        # Click "Place Order" to complete the process
        place_order_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.checkout-button.is-primary")
        ))
        place_order_button.click()

        # Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "h1.checkout-success-title")
        ))
        message_text = success_message.text
        self.assertIn("Thanks for your order!", message_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()