import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080")
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.set_window_size(1200, 800)

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies_button.click()
        except:
            self.fail("Failed to find or click on the accept cookies button.")

        # Navigate to login page
        try:
            account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active")))
            account_button.click()
            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()
        except:
            self.fail("Failed to navigate to login page.")

        # Perform login
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button = driver.find_element(By.XPATH, "//button/span[contains(text(), 'Login')]")
            login_button.click()
        except:
            self.fail("Failed to login.")

        # Add a product to cart
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart'][i[contains(@class, 'fa-shopping-cart')]]")))
            add_to_cart_button.click()
            
            # Open cart popup
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.icon-cart")))
            cart_icon.click()
            view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except:
            self.fail("Failed to add product to cart or navigate to cart page.")
        
        # Proceed to checkout
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except:
            self.fail("Failed to proceed to checkout.")

        # Fill out billing form
        try:
            first_name_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_input = driver.find_element(By.NAME, "lastName")
            street_address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")
            email_input = driver.find_element(By.NAME, "email")

            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            street_address_input.send_keys("123 Test St")
            city_input.send_keys("Testville")
            postal_code_input.send_keys("12345")
            phone_input.send_keys("1234567890")
            email_input.send_keys("test22@user.com")
        except:
            self.fail("Failed to fill billing form.")

        # Verify billing form is filled
        self.assertNotEqual(first_name_input.get_attribute('value'), "", "First Name not filled.")
        self.assertNotEqual(last_name_input.get_attribute('value'), "", "Last Name not filled.")
        self.assertNotEqual(street_address_input.get_attribute('value'), "", "Street Address not filled.")
        self.assertNotEqual(city_input.get_attribute('value'), "", "City not filled.")
        self.assertNotEqual(postal_code_input.get_attribute('value'), "", "Postal Code not filled.")
        self.assertNotEqual(phone_input.get_attribute('value'), "", "Phone not filled.")
        self.assertNotEqual(email_input.get_attribute('value'), "", "Email not filled.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()