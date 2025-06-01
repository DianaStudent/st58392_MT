from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies
        cookie_accept_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(cookie_accept_button.is_displayed())
        cookie_accept_button.click()

        # Log in
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))).click()
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")

        self.assertTrue(email_input.is_displayed() and password_input.is_displayed() and login_button.is_displayed())

        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Add product to cart
        add_to_cart_buttons = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        self.assertTrue(len(add_to_cart_buttons) > 0)
        add_to_cart_buttons[0].click()

        # Open cart and navigate to cart page
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_button.click()
        view_cart_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Click "Proceed to Checkout"
        proceed_to_checkout_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name_input = driver.find_element(By.NAME, "lastName")
        address_input = driver.find_element(By.NAME, "address")
        city_input = driver.find_element(By.NAME, "city")
        postal_code_input = driver.find_element(By.NAME, "postalCode")
        phone_input = driver.find_element(By.NAME, "phone")
        email_input = driver.find_element(By.NAME, "email")
        
        self.assertTrue(
            first_name_input.is_displayed() and 
            last_name_input.is_displayed() and 
            address_input.is_displayed() and 
            city_input.is_displayed() and 
            postal_code_input.is_displayed() and 
            phone_input.is_displayed() and 
            email_input.is_displayed()
        )

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        address_input.send_keys("123 Test Street")
        city_input.send_keys("Test City")
        wait.until(EC.element_to_be_clickable((By.NAME, "postalCode"))).send_keys("12345")
        phone_input.send_keys("1234567890")
        email_input.send_keys("test22@user.com")
        
        # Wait for the region (state) select to appear
        state_dropdown = wait.until(EC.presence_of_element_located((By.NAME, "state")))
        self.assertTrue(state_dropdown.is_displayed())

        # Accept terms and proceed
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, "isAgree")))
        self.assertTrue(terms_checkbox.is_displayed())
        terms_checkbox.click()

        place_order_button = driver.find_element(By.CSS_SELECTOR, ".btn-hover")
        self.assertTrue(place_order_button.is_displayed())
        place_order_button.click()

        # Confirm success
        # Assuming after form submission a confirmation page or order details are displayed to verify form filled successfully
        success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb-content")))
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()