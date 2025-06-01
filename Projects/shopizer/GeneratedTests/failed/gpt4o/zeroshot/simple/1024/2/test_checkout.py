from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button not found: {str(e)}")

        # Navigate to the login page
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active"))
            )
            account_button.click()

            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found: {str(e)}")

        # Perform login
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.CSS_SELECTOR, "div.button-box > button")

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except Exception as e:
            self.fail(f"Login elements not found: {str(e)}")

        # Add product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {str(e)}")

        # Go to the cart page
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.same-style.cart-wrap > button"))
            )
            cart_button.click()

            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"View cart button not found: {str(e)}")

        # Proceed to checkout
        try:
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout button not found: {str(e)}")

        # Fill in billing details
        try:
            first_name_input = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_input = driver.find_element(By.NAME, "lastName")
            address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")

            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            address_input.send_keys("1234 Test Address")
            city_input.send_keys("Test City")
            postal_code_input.send_keys("12345")
            phone_input.send_keys("1234567890")
        except Exception as e:
            self.fail(f"Billing details form not filled: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()