import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.base_url = "http://localhost/"

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        driver.get(self.base_url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "root")))

        # Accept cookies on the home page
        cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # Navigate to the login page
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # Perform login
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        email_input.clear()
        email_input.send_keys("test22@user.com")

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
        password_input.clear()
        password_input.send_keys("test**11")

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Wait for login to complete
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-name")))
        if not welcome_message.text.strip():
            self.fail("Login failed or welcome message not present")

        # Navigate back to home page
        home_link = driver.find_element(By.LINK_TEXT, "Home")
        home_link.click()

        # Hover over the first product and add to cart
        first_product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2:first-child .product-img a")))
        ActionChains(driver).move_to_element(first_product).perform()

        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-wrap-2:first-child .fa-shopping-cart")))
        add_to_cart_button.click()

        # Open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible and click "View cart"
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Click "Proceed to Checkout"
        proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout.click()

        # Fill out the billing form
        self.fill_billing_form(driver, wait)

        # Verify form filled
        billing_address = wait.until(EC.presence_of_element_located((By.ID, "autocomplete")))
        if billing_address.get_attribute("value") != "Street1":
            self.fail("Billing form not filled successfully")

    def fill_billing_form(self, driver, wait):
        company_input = wait.until(EC.presence_of_element_located((By.NAME, "company")))
        company_input.clear()
        company_input.send_keys("Comp1")

        address_input = driver.find_element(By.ID, "autocomplete")
        address_input.clear()
        address_input.send_keys("Street1")

        city_input = driver.find_element(By.NAME, "city")
        city_input.clear()
        city_input.send_keys("Quebec")

        # Select region/state
        state_select = driver.find_element(By.CSS_SELECTOR, "select[name='stateProvince']")
        for option in state_select.find_elements_by_tag_name('option'):
            if option.text == "Quebec":
                option.click()
                break

        postal_code_input = driver.find_element(By.NAME, "postalCode")
        postal_code_input.clear()
        postal_code_input.send_keys("1234")

        phone_input = driver.find_element(By.NAME, "phone")
        phone_input.clear()
        phone_input.send_keys("1234567891")

        accept_terms = driver.find_element(By.XPATH, "//input[@value='false']")
        if not accept_terms.is_selected():
            accept_terms.click()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()