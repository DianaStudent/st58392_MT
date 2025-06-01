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

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to 'Category A'
            category_a_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
            category_a_link.click()

            # Click on 'Product A'
            product_a_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
            product_a_link.click()

            # Click on 'Add to cart'
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
            add_to_cart_button.click()

            # Click on the cart button
            cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']")))
            cart_button.click()

            # Wait for 'Go to checkout' button and click
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "GO TO CHECKOUT")))
            go_to_checkout_button.click()

            # Fill out the checkout form
            email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
            email_input.send_keys("mail@mail.com")

            mobile_input = driver.find_element(By.ID, "customer.mobile")
            mobile_input.send_keys("12345678")

            state_input = driver.find_element(By.ID, "shipping_address.state")
            state_input.send_keys("Riga")

            city_input = driver.find_element(By.ID, "shipping_address.city")
            city_input.send_keys("Riga")

            # Select shipping method
            shipping_method_radio = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
            shipping_method_radio.click()

            # Select payment method
            payment_method_radio = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
            payment_method_radio.click()

            # Click on 'Next'
            next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.button.is-primary")
            next_button.click()

            # Place the order
            place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']")))
            place_order_button.click()

            # Verify thank you message
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]")))
            self.assertIsNotNone(success_message, "Order success message not found")

        except Exception as e:
            self.fail(f"Test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()