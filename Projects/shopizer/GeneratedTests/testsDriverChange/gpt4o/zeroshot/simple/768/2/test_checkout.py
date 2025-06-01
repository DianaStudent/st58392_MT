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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or clickable")

        # Navigate to login
        try:
            account_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active"))
            )
            account_button.click()

            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Navigation to login failed")

        # Perform login
        try:
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Login process failed")

        # Add product to cart from home page
        try:
            add_to_cart_buttons = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[title='Add to cart']"))
            )
            add_to_cart_buttons[0].click()
        except:
            self.fail("Product add to cart failed")

        # View cart page
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.icon-cart"))
            )
            cart_button.click()
        except:
            self.fail("Unable to navigate to cart page")

        # Proceed to checkout
        try:
            proceed_to_checkout_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))
            )
            proceed_to_checkout_link.click()
        except:
            self.fail("Proceed to checkout failed")

        # Verify filling billing form
        try:
            first_name_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = driver.find_element(By.NAME, "lastName")
            address_field = driver.find_element(By.NAME, "address")
            city_field = driver.find_element(By.NAME, "city")
            postal_code_field = driver.find_element(By.NAME, "postalCode")
            phone_field = driver.find_element(By.NAME, "phone")

            # Fill in the billing information with placeholder values
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            address_field.send_keys("123 Test Address")
            city_field.send_keys("Test City")
            postal_code_field.send_keys("123456")
            phone_field.send_keys("1234567890")
        except:
            self.fail("Billing form filling failed")

        # Verify filled billing fields
        if not all([first_name_field.get_attribute("value"), last_name_field.get_attribute("value"),
                    address_field.get_attribute("value"), city_field.get_attribute("value"), 
                    postal_code_field.get_attribute("value"), phone_field.get_attribute("value")]):
            self.fail("Billing form not correctly filled")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()