from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
        cookies_button.click()

        # Log in
        account_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'account-setting-active')))
        account_button.click()
        login_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()
        
        email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        email_input.send_keys('test22@user.com')
        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys('test**11')
        login_submit = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        login_submit.click()

        # Add product to the cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Open cart and go to cart page
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-cart')))
        cart_button.click()
        view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Proceed to checkout
        proceed_to_checkout = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout.click()

        # Fill in the billing form
        billing_first_name = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        billing_first_name.send_keys("Test")
        billing_last_name = driver.find_element(By.NAME, "lastName")
        billing_last_name.send_keys("User")
        billing_address = driver.find_element(By.NAME, "address")
        billing_address.send_keys("123 Test Street")
        billing_city = driver.find_element(By.NAME, "city")
        billing_city.send_keys("Test City")

        # Wait for region select to appear dynamically
        billing_country = driver.find_element(By.NAME, "country")
        billing_country.send_keys("Canada")
        billing_state = self.wait.until(EC.element_to_be_clickable((By.NAME, "stateProvince")))
        billing_state.send_keys("Quebec")

        billing_zip = driver.find_element(By.NAME, "postalCode")
        billing_zip.send_keys("H2H 2H2")
        billing_phone = driver.find_element(By.NAME, "phone")
        billing_phone.send_keys("8888888888")
        billing_email = driver.find_element(By.NAME, "email")
        billing_email.send_keys("test22@user.com")

        # Accept terms and place order
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()
        place_order_btn = driver.find_element(By.XPATH, "//button[text()='Place your order']")
        place_order_btn.click()

        # Confirm success if form is filled
        self.assertIn("Checkout", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()