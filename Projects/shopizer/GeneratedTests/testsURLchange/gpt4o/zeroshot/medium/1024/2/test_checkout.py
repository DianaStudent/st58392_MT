from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open home page and accept cookies
        accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
        accept_cookies_button.click()
        
        # Step 2: Log in with provided credentials
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))).click()
        login_button = driver.find_element(By.LINK_TEXT, "Login")
        if not login_button or not login_button.is_displayed():
            self.fail("Login button is not present or visible.")
        login_button.click()

        username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = driver.find_element(By.NAME, "loginPassword")
        if not username_field or not password_field:
            self.fail("Username or password field is missing.")
        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")

        driver.find_element(By.XPATH, "//button/span[text()='Login']").click()

        # Step 3: Add product to the cart
        product_add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//h3/a[text()='Olive Table']/parent::div/following-sibling::div/button"))
        )
        product_add_to_cart_button.click()

        # Step 4: Open cart and navigate to cart page
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_button.click()
        view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Step 5: Click "Proceed to Checkout"
        proceed_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Step 6: Fill in the billing form
        first_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_field = driver.find_element(By.NAME, "lastName")
        address_field = driver.find_element(By.NAME, "address")
        city_field = driver.find_element(By.NAME, "city")
        postal_code_field = driver.find_element(By.NAME, "postalCode")
        phone_field = driver.find_element(By.NAME, "phone")

        for field in [first_name_field, last_name_field, address_field, city_field, postal_code_field, phone_field]:
            if not field:
                self.fail("A required billing field is missing or not visible.")
        
        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        address_field.send_keys("1234 Street")
        city_field.send_keys("My City")
        postal_code_field.send_keys("H2H 2H2")
        phone_field.send_keys("8888888888")

        # Step 7: Accept terms and proceed
        terms_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))
        if not terms_checkbox:
            self.fail("Terms agreement checkbox is missing.")
        terms_checkbox.click()
        
        place_order_button = driver.find_element(By.XPATH, "//button[text()='Place your order']")
        if not place_order_button:
            self.fail("Place order button is missing.")
        place_order_button.click()

        # Step 8: Confirm success if form is filled
        confirm_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        if not confirm_name_field or confirm_name_field.get_attribute("value") != "Test":
            self.fail("Form was not submitted correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()