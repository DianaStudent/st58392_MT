from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Accept cookies
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found or not clickable: {str(e)}")

        # Step 2: Log in
        try:
            account_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            email_input.send_keys("test22@user.com")

            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")

            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            login_button.click()
        except Exception as e:
            self.fail(f"Login failed: {str(e)}")

        # Step 3: Add a product to the cart
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-action-2']/button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {str(e)}")

        # Step 4: View cart
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()

            view_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"View cart button not found or not clickable: {str(e)}")

        # Step 5: Proceed to checkout
        try:
            proceed_to_checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            proceed_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Proceed to checkout button not found or not clickable: {str(e)}")

        # Step 6: Fill in the billing form
        try:
            first_name_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            )
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("User")

            address_input = driver.find_element(By.NAME, "address")
            address_input.send_keys("1234 Street address")

            city_input = driver.find_element(By.NAME, "city")
            city_input.send_keys("My City")

            postal_code_input = driver.find_element(By.NAME, "postalCode")
            postal_code_input.send_keys("H2H-2H2")

            phone_input = driver.find_element(By.NAME, "phone")
            phone_input.send_keys("8888888888")

            email_input = driver.find_element(By.NAME, "email")
            email_input.send_keys("test22@user.com")

            country_select = driver.find_element(By.XPATH, "//select[@name='country']")
            country_select.click()

            # Step 7: Accept terms
            accept_terms_checkbox = driver.find_element(By.NAME, "isAgree")
            accept_terms_checkbox.click()

            place_order_button = driver.find_element(By.XPATH, "//button[text()='Place your order']")
            place_order_button.click()
        except Exception as e:
            self.fail(f"Failed to fill in the billing form or place order: {str(e)}")

        # Step 8: Confirm success
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/checkout")
            )
            success_message = driver.find_element(By.XPATH, "//h3[text()='Your order']")
            self.assertIsNotNone(success_message, "Billing form not filled successfully")
        except Exception as e:
            self.fail(f"Billing form submission failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()