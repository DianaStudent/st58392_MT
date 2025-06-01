from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserCheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def element_exists(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def test_user_checkout(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except TimeoutException:
            self.fail("Cookie consent button not found.")

        # Open Login page
        try:
            account_setting = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_setting.click()
            login_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_button.click()
        except TimeoutException:
            self.fail("Login link not found.")

        # Perform login
        try:
            email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            email_input.send_keys("test22@user.com")
            password_input = driver.find_element(By.CLASS_NAME, "user-password")
            password_input.send_keys("test**11")
            password_input.send_keys(Keys.RETURN)
        except TimeoutException:
            self.fail("Login form elements not found.")

        # Add product to the cart
        try:
            add_to_cart_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//button[@title='Add to cart'])[1]")))
            add_to_cart_btn.click()
        except TimeoutException:
            self.fail("Add to Cart button not found.")

        # Open the cart pop-up
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
            view_cart = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart.click()
        except TimeoutException:
            self.fail("Cart view not accessible.")

        # Proceed to checkout
        try:
            proceed_to_checkout = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            proceed_to_checkout.click()
        except TimeoutException:
            self.fail("Proceed to Checkout button not found.")

        # Fill in the billing form
        try:
            first_name = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            first_name.send_keys("John")
            last_name = driver.find_element(By.NAME, "lastName")
            last_name.send_keys("Doe")
            address = driver.find_element(By.NAME, "address")
            address.send_keys("123 Testing St")

            # Wait for region (state) select to appear dynamically
            region_select = self.wait.until(EC.presence_of_element_located((By.NAME, "stateProvince")))
            region_select.send_keys("Quebec")

            city = driver.find_element(By.NAME, "city")
            city.send_keys("Montreal")
            postal_code = driver.find_element(By.NAME, "postalCode")
            postal_code.send_keys("H1A 1A1")
            phone = driver.find_element(By.NAME, "phone")
            phone.send_keys("1234567890")
            email = driver.find_element(By.NAME, "email")
            email.send_keys("john.doe@example.com")
        except TimeoutException:
            self.fail("Billing form elements not accessible.")

        # Accept terms and proceed
        try:
            terms_checkbox = driver.find_element(By.NAME, "isAgree")
            terms_checkbox.click()
            place_order_btn = driver.find_element(By.CSS_SELECTOR, ".btn-hover")
            place_order_btn.click()
        except TimeoutException:
            self.fail("Unable to locate terms acceptance and place order button.")

        # Confirm form submission success
        if not self.element_exists(By.NAME, "firstName") or first_name.get_attribute("value") != "John":
            self.fail("Billing form not filled correctly.")

if __name__ == "__main__":
    unittest.main()