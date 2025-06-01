import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_checkout_process(self):
        driver = self.driver

        # Accept Cookies
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            accept_cookies.click()
        except:
            self.fail("Cookie accept button not found.")

        # Log in
        try:
            account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.account-setting-active')))
            account_button.click()
            login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
            login_link.click()
            email_field = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
            password_field = driver.find_element(By.NAME, 'loginPassword')
            email_field.send_keys('test22@user.com')
            password_field.send_keys('test**11')
            login_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
            login_button.click()
        except:
            self.fail("Login process failed.")

        # Add product to cart
        try:
            add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[title="Add to cart"]')))
            if not add_to_cart_buttons:
                self.fail("Add to cart buttons not found.")
            add_to_cart_buttons[0].click()
        except:
            self.fail("Failed to add product to cart.")

        # Open cart and navigate to cart page
        try:
            cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.icon-cart')))
            ActionChains(driver).move_to_element(cart_button).perform()
            view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'View Cart')))
            view_cart_button.click()
        except:
            self.fail("Cannot view cart.")

        # Click "Proceed to Checkout"
        try:
            proceed_to_checkout = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Proceed to Checkout')))
            proceed_to_checkout.click()
        except:
            self.fail("Proceed to Checkout button not found.")

        # Fill in the billing form
        try:
            first_name = self.wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
            last_name = driver.find_element(By.NAME, 'lastName')
            address = driver.find_element(By.ID, 'autocomplete')
            city = driver.find_element(By.NAME, 'city')
            postal_code = driver.find_element(By.NAME, 'postalCode')
            phone = driver.find_element(By.NAME, 'phone')
            email = driver.find_element(By.NAME, 'email')

            first_name.send_keys('John')
            last_name.send_keys('Doe')
            address.send_keys('123 Billing St')
            city.send_keys('Billing City')
            postal_code.send_keys('12345')
            phone.send_keys('1234567890')
            email.send_keys('test22@user.com')
            
            billing_state = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select[name="state"]')))
            billing_state.click()
            billing_state.send_keys(Keys.ARROW_DOWN, Keys.ENTER) 

            terms_checkbox = driver.find_element(By.NAME, 'isAgree')
            terms_checkbox.click()

            place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-hover')))
            place_order_button.click()

            # Verify form filled
            self.assertTrue(first_name.get_attribute('value'), "Billing form is not filled properly.")

        except:
            self.fail("Failed to fill billing info.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()