import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies.click()
        except:
            pass

        # Navigate to login page from header
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.account-setting-active')))
        account_button.click()
        
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_button.click()

        # Log in using credentials
        email_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        email_input.clear()
        email_input.send_keys("test22@user.com")

        password_input = driver.find_element(By.NAME, 'loginPassword')
        password_input.clear()
        password_input.send_keys("test**11")

        login_submit = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
        login_submit.click()

        # Verify user is logged in by checking user name
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.user-name'), 'Welcome Test User'))

        # Navigate back to home page
        home_link = driver.find_element(By.LINK_TEXT, 'Home')
        home_link.click()

        # Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()

        # Click "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Open cart popup
        cart_icon_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.icon-cart')))
        cart_icon_button.click()

        # Wait for popup and click on "View Cart"
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'View Cart')))
        view_cart_button.click()

        # On the cart page, click "Proceed to Checkout" button
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Proceed to Checkout')))
        proceed_to_checkout_button.click()

        # Fill out the billing form
        # Company
        company_input = wait.until(EC.presence_of_element_located((By.NAME, 'company')))
        company_input.clear()
        company_input.send_keys("Comp1")

        # Address
        address_input = driver.find_element(By.NAME, 'address')
        address_input.clear()
        address_input.send_keys("Street1")

        # City
        city_input = driver.find_element(By.NAME, 'city')
        city_input.clear()
        city_input.send_keys("Quebec")

        # Select state
        state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='State']]/option[@value='QC']")))
        state_select.click()

        # Postal code
        postal_code_input = driver.find_element(By.NAME, 'postalCode')
        postal_code_input.clear()
        postal_code_input.send_keys("1234")

        # Phone number
        phone_number_input = driver.find_element(By.NAME, 'phone')
        phone_number_input.clear()
        phone_number_input.send_keys("1234567891")

        # Accept terms and conditions
        accept_terms_checkbox = driver.find_element(By.NAME, 'isAgree')
        if not accept_terms_checkbox.is_selected():
            accept_terms_checkbox.click()

        # Confirm the form is filled
        try:
            billing_form_filled = all([
                company_input.get_attribute('value') == 'Comp1',
                address_input.get_attribute('value') == 'Street1',
                city_input.get_attribute('value') == 'Quebec',
                postal_code_input.get_attribute('value') == '1234',
                phone_number_input.get_attribute('value') == '1234567891',
                accept_terms_checkbox.is_selected()
            ])
            self.assertTrue(billing_form_filled, "Billing form was not filled correctly.")
        except Exception as e:
            self.fail(f"Billing form verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()