import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_user_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Close cookie consent if present
        try:
            accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
            accept_cookies_button.click()
        except:
            pass

        # Step 2: Log in using the provided credentials
        account_setting_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_setting_button.click()
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.XPATH, "//button[span[text()='Login']]")

        self.assertTrue(username_input)
        self.assertTrue(password_input)
        self.assertTrue(login_button)

        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Step 3: Add product to the cart
        product_add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        product_add_to_cart_button.click()

        # Step 4: Open the cart and navigate to the cart page
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Step 5: Click "Proceed to Checkout"
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Step 6: Fill in the billing form
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_input = driver.find_element(By.NAME, "lastName")
        address_input = driver.find_element(By.NAME, "address")
        city_input = driver.find_element(By.NAME, "city")
        postal_code_input = driver.find_element(By.NAME, "postalCode")
        phone_input = driver.find_element(By.NAME, "phone")
        email_input = driver.find_element(By.NAME, "email")

        self.assertTrue(first_name_input)
        self.assertTrue(last_name_input)
        self.assertTrue(address_input)
        self.assertTrue(city_input)
        self.assertTrue(postal_code_input)
        self.assertTrue(phone_input)
        self.assertTrue(email_input)

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        address_input.send_keys("1234 Test St")
        city_input.send_keys("Test City")
        postal_code_input.send_keys("H2H-2H2")
        phone_input.send_keys("8888888888")
        email_input.send_keys("test22@user.com")

        # Wait for state selection to become available
        state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='region']")))
        self.assertTrue(state_select)

        # Step 7: Accept terms and proceed
        accept_terms_checkbox = driver.find_element(By.NAME, "isAgree")
        place_order_button = driver.find_element(By.CSS_SELECTOR, ".place-order button")

        self.assertTrue(accept_terms_checkbox)
        self.assertTrue(place_order_button)

        accept_terms_checkbox.click()
        place_order_button.click()

        # Step 8: Confirm success if form is filled
        self.assertTrue(first_name_input.get_attribute('value') == "Test")
        self.assertTrue(last_name_input.get_attribute('value') == "User")
        self.assertTrue(address_input.get_attribute('value') == "1234 Test St")
        self.assertTrue(city_input.get_attribute('value') == "Test City")

if __name__ == "__main__":
    unittest.main()