import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Cookie consent button not found.")

        # Navigate to login page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active")))
            account_button.click()
            login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_button.click()
        except:
            self.fail("Navigation to login page failed.")

        # Perform login
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            email_input.send_keys("test22@user.com")
            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")
            login_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_submit.click()
        except:
            self.fail("Login form elements not found.")

        # Add product to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found.")

        # Proceed to cart page
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.header-right-wrap button.icon-cart")))
            cart_button.click()
            view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except:
            self.fail("Navigation to cart page failed.")

        # Proceed to checkout
        try:
            checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except:
            self.fail("Checkout button not found.")

        # Fill billing form
        try:
            first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_input = driver.find_element(By.NAME, "lastName")
            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")

            # Verify form filled
            self.assertEqual(first_name_input.get_attribute("value"), "John", "First name not filled correctly.")
            self.assertEqual(last_name_input.get_attribute("value"), "Doe", "Last name not filled correctly.")
        except:
            self.fail("Billing form elements not found or not filled correctly.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()