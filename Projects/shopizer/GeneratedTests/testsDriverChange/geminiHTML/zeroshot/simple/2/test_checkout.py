import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            pass

        # Go to login page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        # Login
        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )

            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Login elements not found or could not be interacted with")

        # Add product to cart (Olive Table)
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button for Olive Table not found")

        # Add product to cart (Chair)
        try:
            add_to_cart_button_chair = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button_chair.click()
        except:
            self.fail("Add to cart button for Chair not found")

        # Go to cart page
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()

            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except:
            self.fail("Cart button or View Cart button not found")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # Fill billing details
        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            address_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            postal_code_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )

            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            address_field.send_keys("123 Test Street")
            city_field.send_keys("Test City")
            postal_code_field.send_keys("H2H2H2")
            phone_field.send_keys("8888888888")
            email_field.send_keys("test@test.com")

            # Verify that the billing form is filled
            self.assertEqual(first_name_field.get_attribute("value"), "Test")
            self.assertEqual(last_name_field.get_attribute("value"), "User")
            self.assertEqual(address_field.get_attribute("value"), "123 Test Street")
            self.assertEqual(city_field.get_attribute("value"), "Test City")
            self.assertEqual(postal_code_field.get_attribute("value"), "H2H2H2")
            self.assertEqual(phone_field.get_attribute("value"), "8888888888")
            self.assertEqual(email_field.get_attribute("value"), "test@test.com")

        except:
            self.fail("Billing details elements not found or could not be interacted with")

if __name__ == "__main__":
    unittest.main()