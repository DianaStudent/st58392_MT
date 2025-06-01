from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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

        # Login
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
            )

            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()

        except:
            self.fail("Login form elements not found")

        # Add items to cart
        try:
            add_to_cart_buttons = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[title='Add to cart']"))
            )
            add_to_cart_buttons[0].click()
            WebDriverWait(driver, 5)
            add_to_cart_buttons[1].click()
            WebDriverWait(driver, 5)
        except:
            self.fail("Add to cart buttons not found")
        
        # View cart
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # Fill billing form
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
            address_field.send_keys("123 Street")
            city_field.send_keys("Mycity")
            postal_code_field.send_keys("H2H2H2")
            phone_field.send_keys("1234567890")
            email_field.send_keys("test@example.com")
        except:
            self.fail("Billing form elements not found")
        
        # Verify that the billing form is filled
        self.assertEqual(first_name_field.get_attribute("value"), "Test")
        self.assertEqual(last_name_field.get_attribute("value"), "User")
        self.assertEqual(address_field.get_attribute("value"), "123 Street")
        self.assertEqual(city_field.get_attribute("value"), "Mycity")
        self.assertEqual(postal_code_field.get_attribute("value"), "H2H2H2")
        self.assertEqual(phone_field.get_attribute("value"), "1234567890")
        self.assertEqual(email_field.get_attribute("value"), "test@example.com")

if __name__ == "__main__":
    unittest.main()