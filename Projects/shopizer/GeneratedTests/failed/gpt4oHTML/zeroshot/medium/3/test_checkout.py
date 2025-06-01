from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # 1. Open the home page and accept cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies.is_displayed(), "Accept cookies button not found")
            accept_cookies.click()
        except:
            self.fail("Failed to find and click accept cookies")

        # 2. Log in using the provided credentials
        try:
            account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
            account_button.click()

            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()

            username_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Login']")))

            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Failed to log in using provided credentials")

        # 3. Add product to the cart
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-img")))
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@title='Add to cart'])[1]")))
            add_to_cart_button.click()
        except:
            self.fail("Failed to add product to the cart")

        # 4. Open the cart and navigate to the cart page
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
            cart_button.click()
            view_cart_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_link.click()
        except:
            self.fail("Failed to open the cart and navigate to the cart page")

        # 5. Click "Proceed to Checkout"
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except:
            self.fail("Failed to click 'Proceed to Checkout'")

        # 6. Fill in the billing form
        try:
            first_name_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
            last_name_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "lastName")))
            address_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "address")))
            city_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "city")))
            postal_code_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "postalCode")))
            phone_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "phone")))
            email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))

            first_name_input.send_keys("John")
            last_name_input.send_keys("Doe")
            address_input.send_keys("123 Elm Street")
            city_input.send_keys("Metropolis")
            postal_code_input.send_keys("12345")
            phone_input.send_keys("1234567890")
            email_input.send_keys("john.doe@example.com")

            # State will appear after address is filled
            state_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='state']/option[2]")))
            state_select.click()
        except:
            self.fail("Failed to fill in the billing information")

        # 7. Accept terms and proceed
        try:
            terms_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "isAgree")))
            terms_checkbox.click()

            place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']")))
            place_order_button.click()
        except:
            self.fail("Failed to accept terms and proceed")

        # 8. Confirm success
        self.assertTrue(first_name_input.get_attribute('value'), "Billing information was not saved successfully")

    def tearDown(self):
        self.driver.quit()