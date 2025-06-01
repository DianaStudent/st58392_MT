import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click 'Accept cookies' button
        accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies.click()

        # Go to Login Page
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Enter email and password
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")

        # Click Login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']")))
        login_button.click()

        # Add Olive Table to the cart
        olive_table_add_to_cart = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following-sibling::div/button[@title='Add to cart']"))
        )
        olive_table_add_to_cart.click()

        # Open Cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_button.click()

        # Proceed to Checkout
        proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed to Checkout']")))
        proceed_to_checkout.click()

        # Fill in the billing form
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        address_input = wait.until(EC.presence_of_element_located((By.NAME, "address")))
        city_input = wait.until(EC.presence_of_element_located((By.NAME, "city")))
        postal_code_input = wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        address_input.send_keys("123 Test Street")
        city_input.send_keys("TestCity")
        postal_code_input.send_keys("12345")
        phone_input.send_keys("1234567890")

        # Check that billing form is filled
        self.assertEqual(first_name_input.get_attribute('value'), "Test")
        self.assertEqual(last_name_input.get_attribute('value'), "User")
        self.assertEqual(address_input.get_attribute('value'), "123 Test Street")
        self.assertEqual(city_input.get_attribute('value'), "TestCity")
        self.assertEqual(postal_code_input.get_attribute('value'), "12345")
        self.assertEqual(phone_input.get_attribute('value'), "1234567890")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()