import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
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
            self.fail("Accept cookies button not found")

        # Navigate to login page
        try:
            account_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        # Perform login
        try:
            username_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Login form elements not found")

        # Add products to cart
        try:
            add_to_cart_buttons = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[@title='Add to cart']"))
            )
            for button in add_to_cart_buttons:
                button.click()
        except:
            self.fail("Add to cart buttons not available")

        # Go to the cart page
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Click "Proceed to Checkout"
        try:
            checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # Fill in the billing form
        try:
            first_name = self.wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name = driver.find_element(By.NAME, "lastName")
            address = driver.find_element(By.NAME, "address")
            city = driver.find_element(By.NAME, "city")
            postal_code = driver.find_element(By.NAME, "postalCode")
            phone = driver.find_element(By.NAME, "phone")
            email = driver.find_element(By.NAME, "email")

            first_name.send_keys("Test")
            last_name.send_keys("User")
            address.send_keys("1234 Test Address")
            city.send_keys("Test City")
            postal_code.send_keys("T1E 4N1")
            phone.send_keys("1234567890")
            email.send_keys("test22@user.com")

            self.assertEqual(first_name.get_attribute("value"), "Test")
            self.assertEqual(last_name.get_attribute("value"), "User")
            self.assertEqual(address.get_attribute("value"), "1234 Test Address")
            self.assertEqual(city.get_attribute("value"), "Test City")
            self.assertEqual(postal_code.get_attribute("value"), "T1E 4N1")
            self.assertEqual(phone.get_attribute("value"), "1234567890")
            self.assertEqual(email.get_attribute("value"), "test22@user.com")

        except:
            self.fail("Billing form elements not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()