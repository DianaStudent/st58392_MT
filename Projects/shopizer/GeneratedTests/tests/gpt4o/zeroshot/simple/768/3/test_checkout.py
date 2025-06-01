import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail("Cookie acceptance button not found or clickable.")

        # Go to login page
        try:
            account_setting_button = driver.find_element(By.CSS_SELECTOR, ".account-setting-active")
            account_setting_button.click()
            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail("Login link not found or clickable.")

        # Perform login
        try:
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")

            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except Exception as e:
            self.fail("Login form elements not found.")

        # Add product to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart button not found or clickable.")

        # Go to cart and proceed to checkout
        try:
            view_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_link.click()
            checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except Exception as e:
            self.fail("Cart view or checkout button not found or clickable.")

        # Fill in billing form
        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            last_name_input = driver.find_element(By.NAME, "lastName")
            address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")
            email_input = driver.find_element(By.NAME, "email")

            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")
            address_input.send_keys("1234 Elm Street")
            city_input.send_keys("Townsville")
            postal_code_input.send_keys("12345")
            phone_input.send_keys("1234567890")
            email_input.send_keys("test22@user.com")
        except Exception as e:
            self.fail("Billing form elements not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()