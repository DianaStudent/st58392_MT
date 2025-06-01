import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://localhost/"

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get(self.base_url)
        
        # Accept cookies if the button exists
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            cookie_button.click()
        except:
            pass

        # Step 2: Log in using the provided credentials
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_button.click()

        # Ensure login form is present
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-password')))

        self.assertTrue(username_input and username_input.is_displayed(), "Login form not loaded properly.")
        username_input.send_keys("test22@user.com")

        self.assertTrue(password_input and password_input.is_displayed(), "Password input not available.")
        password_input.send_keys("test**11")

        login_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_submit.click()

        # Step 3: Add product to the cart
        # Assuming the first product has an 'Add to cart' button readily available.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Step 4: Open the cart and navigate to the cart page
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-cart')))
        cart_icon.click()

        view_cart = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart.click()

        # Step 5: Click "Proceed to Checkout"
        proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout.click()

        # Step 6: Fill in the billing form
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, 'lastName')))
        address_input = wait.until(EC.presence_of_element_located((By.ID, 'autocomplete')))
        city_input = wait.until(EC.presence_of_element_located((By.NAME, 'city')))
        postal_code_input = wait.until(EC.presence_of_element_located((By.NAME, 'postalCode')))
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, 'phone')))
        email_input = wait.until(EC.presence_of_element_located((By.NAME, 'email')))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        address_input.send_keys("1234 Test Address")
        city_input.send_keys("TestCity")
        postal_code_input.send_keys("123456")
        phone_input.send_keys("1234567890")
        email_input.send_keys("test22@user.com")

        # Wait for region (state) select to appear dynamically after filling address
        region_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[not(@disabled)]")))
        region_select.click()
        region_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']")))
        region_option.click()

        # Step 7: Accept terms and proceed
        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, 'isAgree')))
        terms_checkbox.click()

        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Place your order')]")))

        # Step 8: Confirm success if form is filled
        if not all([first_name_input.get_attribute('value'), last_name_input.get_attribute('value'),
                    address_input.get_attribute('value'), city_input.get_attribute('value'),
                    postal_code_input.get_attribute('value'), phone_input.get_attribute('value'),
                    email_input.get_attribute('value')]):
            self.fail("Billing form is not completely filled.")

        place_order_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()