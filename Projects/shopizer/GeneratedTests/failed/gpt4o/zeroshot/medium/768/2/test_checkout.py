from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        accept_cookies_button = wait.until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookies_button.click()

        # Navigate to login page
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()
        login_link = driver.find_element(By.LINK_TEXT, "Login")
        login_link.click()

        # Perform login
        username_input = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-box button")

        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Add product to cart
        product_add_to_cart_buttons = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-action-2 .fa-shopping-cart"))
        )
        self.assertTrue(product_add_to_cart_buttons, "Add to Cart buttons are not present")
        product_add_to_cart_buttons[0].click()

        # Wait for cart popup to be active and proceed to cart page
        cart_view_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
        )
        cart_view_button.click()

        # Verify we're on cart page and proceed to checkout
        proceed_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
        )
        proceed_to_checkout_button.click()

        # Fill out billing form
        first_name_input = wait.until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        
        # Ensure all elements exist before filling
        last_name_input = driver.find_element(By.NAME, "lastName")
        address_input = driver.find_element(By.NAME, "address")
        city_input = driver.find_element(By.NAME, "city")
        postal_code_input = driver.find_element(By.NAME, "postalCode")
        phone_input = driver.find_element(By.NAME, "phone")
        email_input = driver.find_element(By.NAME, "email")

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        address_input.send_keys("1234 Elm Street")
        city_input.send_keys("Metropolis")
        postal_code_input.send_keys("12345")
        phone_input.send_keys("1234567890")
        email_input.clear()
        email_input.send_keys("johndoe@example.com")
        
        # Wait for the state to dynamically appear, then select
        state_select_element = wait.until(
            EC.presence_of_element_located((By.NAME, "state"))
        )
        Select(state_select_element).select_by_visible_text("Quebec")

        # Agree to terms
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()

        # Place order
        place_order_button = driver.find_element(By.CSS_SELECTOR, ".btn-hover")
        place_order_button.click()

        # Confirm that billing info is filled
        self.assertIn("Billing Details", driver.page_source, "Billing form was not filled.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()