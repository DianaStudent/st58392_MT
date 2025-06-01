import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost/"
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # Accept cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Accept cookies button not found")

        # Log in
        try:
            account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
            account_button.click()

            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_link.click()

            email_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            email_field.send_keys("test22@user.com")

            password_field = driver.find_element(By.NAME, "loginPassword")
            password_field.send_keys("test**11")

            login_button = driver.find_element(By.XPATH, "//button[contains(span, 'Login')]")
            login_button.click()
        except:
            self.fail("Login elements not found")

        # Add product to the cart
        try:
            add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".fa.fa-shopping-cart")))
            add_to_cart_buttons[0].click()  # Adding the first product to the cart
        except:
            self.fail("Add to cart buttons not found")

        # Open the cart popup
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_button.click()

            view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except:
            self.fail("Cart elements not found")

        # Click "Proceed to Checkout"
        try:
            proceed_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            proceed_to_checkout_button.click()
        except:
            self.fail("Proceed to Checkout button not found")

        # Fill in the billing form
        try:
            first_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            first_name_field.send_keys("Test")

            last_name_field = driver.find_element(By.NAME, "lastName")
            last_name_field.send_keys("User")

            address_field = driver.find_element(By.NAME, "address")
            address_field.send_keys("1234 Street address")

            country_select = driver.find_element(By.CSS_SELECTOR, "select[name='country']")
            country_select.send_keys("Canada")

            state_select = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='state']")))
            state_select.send_keys("Quebec")

            city_field = driver.find_element(By.NAME, "city")
            city_field.send_keys("My city")

            postal_code_field = driver.find_element(By.NAME, "postalCode")
            postal_code_field.send_keys("H2H-2H2")

            phone_field = driver.find_element(By.NAME, "phone")
            phone_field.send_keys("1234567890")
        except:
            self.fail("Billing form elements not found")

        # Accept terms and proceed
        try:
            accept_terms_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))
            accept_terms_checkbox.click()

            place_order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Place your order')]")
            place_order_button.click()
        except:
            self.fail("Place order elements not found")

        # Confirm success
        form_filled = driver.find_element(By.NAME, "firstName").get_attribute("value")
        self.assertTrue(form_filled, "Billing form not filled or checkout failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()