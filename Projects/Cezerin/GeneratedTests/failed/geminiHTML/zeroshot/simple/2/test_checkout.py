import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Navigate to Product A page
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Product A page: {e}")

        # 2. Add Product A to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {e}")

        # 3. Click the cart button
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click cart button: {e}")

        # 4. Click "Go to checkout" button
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to click 'Go to checkout' button: {e}")

        # 5. Fill customer details form
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
            email_field.send_keys("mail@mail.com")

            mobile_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.mobile"))
            )
            mobile_field.send_keys("12345678")

            state_field = wait.until(
                EC.presence_of_element_located((By.ID, "shipping_address.state"))
            )
            state_field.send_keys("Riga")

            city_field = wait.until(
                EC.presence_of_element_located((By.ID, "shipping_address.city"))
            )
            city_field.send_keys("Riga")

            # Select shipping method
            shipping_method_radio = wait.until(
                EC.element_to_be_clickable((By.NAME, "shipping_method_id"))
            )
            shipping_method_radio.click()

            # Select payment method
            payment_method_radio = wait.until(
                EC.element_to_be_clickable((By.NAME, "payment_method_id"))
            )
            payment_method_radio.click()

            next_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.is-primary"))
            )
            next_button.click()

        except Exception as e:
            self.fail(f"Failed to fill customer details form: {e}")

        # 6. Fill shipping details form
        try:
            place_order_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.is-primary"))
            )
            place_order_button.click()
        except Exception as e:
            self.fail(f"Failed to fill shipping details form: {e}")

        # 7. Verify success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "checkout-success-title"))
            )
            self.assertIn("Thanks for your order!", success_message.text)
        except Exception as e:
            self.fail(f"Failed to verify success message: {e}")


if __name__ == "__main__":
    unittest.main()