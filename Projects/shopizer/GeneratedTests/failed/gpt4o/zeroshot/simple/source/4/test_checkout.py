from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail("Failed to find Accept Cookies button: " + str(e))

        # Navigate to login page
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()

            login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except Exception as e:
            self.fail("Failed to navigate to login page: " + str(e))

        # Perform login
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button[span='Login']")

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except Exception as e:
            self.fail("Failed to login: " + str(e))

        # Add product to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Failed to add product to cart: " + str(e))

        # Go to cart page
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_button.click()

            view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except Exception as e:
            self.fail("Failed to go to cart page: " + str(e))

        # Proceed to checkout
        try:
            proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            proceed_to_checkout_button.click()
        except Exception as e:
            self.fail("Failed to proceed to checkout: " + str(e))

        # Fill in billing form
        try:
            first_name_input = wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
            last_name_input = driver.find_element(By.NAME, "lastName")
            address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postcode_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")
            email_input = driver.find_element(By.NAME, "email")

            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")
            address_input.send_keys("123 Main Street")
            city_input.send_keys("YourCity")
            postcode_input.send_keys("98765")
            phone_input.send_keys("1234567890")
            email_input.send_keys("test22@user.com")
        except Exception as e:
            self.fail("Failed to fill in billing form: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()