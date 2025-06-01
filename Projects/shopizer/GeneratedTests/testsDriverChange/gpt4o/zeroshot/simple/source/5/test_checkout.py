import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout_process(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except Exception as e:
            self.fail(f"Failed at accepting cookies: {str(e)}")

        # Navigate to login page and login
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_button.click()

            username_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")

            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")

            submit_button = driver.find_element(By.XPATH, '//button/span[text()="Login"]')
            submit_button.click()
        except Exception as e:
            self.fail(f"Failed at login: {str(e)}")

        # Verify login successful
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "user-profile"))
            )
        except Exception as e:
            self.fail("Login verification failed")

        # Add products to cart
        try:
            add_to_cart_buttons = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//button[@title="Add to cart"]'))
            )
            add_to_cart_buttons[0].click()

            # Wait for cart to update
            self.wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'count-style'), '1')
            )
        except Exception as e:
            self.fail(f"Failed at adding product to cart: {str(e)}")

        # Go to cart page
        try:
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()

            proceed_to_checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//a[text()="Proceed to Checkout"]'))
            )
            proceed_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Failed at navigating to cart or checkout: {str(e)}")

        # Fill in billing form
        try:
            billing_info = [
                ("firstName", "Test"),
                ("lastName", "User"),
                ("address", "123 Main St"),
                ("city", "My City"),
                ("postalCode", "H2H-2H2"),
                ("email", "test22@user.com"),
                ("phone", "8888888888")
            ]

            for name, value in billing_info:
                input_field = self.wait.until(
                    EC.presence_of_element_located((By.NAME, name))
                )
                input_field.clear()
                input_field.send_keys(value)

            # Check if billing form is filled
            self.assertTrue(all([
                driver.find_element(By.NAME, name).get_attribute('value') == value
                for name, value in billing_info
            ]), "Billing form was not filled correctly")

        except Exception as e:
            self.fail(f"Failed at filling billing form: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()