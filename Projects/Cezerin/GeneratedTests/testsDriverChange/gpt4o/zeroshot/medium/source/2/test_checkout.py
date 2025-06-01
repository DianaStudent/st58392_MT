from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open product category
        category_a_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.primary-nav .cat-parent a[href="/category-a"]'))
        )
        category_a_link.click()

        # Select the first product
        product_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.products .product-name'))
        )
        product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button'))
        )
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button'))
        )
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.button.is-primary'))
        )
        self.assertTrue(go_to_checkout_button, "GO TO CHECKOUT button is not present")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="email"]'))
        )
        email_input.send_keys("mail@mail.com")

        mobile_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="mobile"]'))
        )
        mobile_input.send_keys("12345678")

        state_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="shipping_address.state"]'))
        )
        state_input.send_keys("Riga")

        city_input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="shipping_address.city"]'))
        )
        city_input.send_keys("Riga")

        # Select a shipping and payment method
        shipping_method = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="shipping_method_id"]'))
        )
        shipping_method.click()

        payment_method = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="payment_method_id"]'))
        )
        payment_method.click()

        # Click "Next" and then "Place Order" to complete the process
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        next_button.click()

        place_order_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        place_order_button.click()

        # Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Thanks for your order!')]"))
        )
        self.assertTrue(success_message, "Success message not found")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()