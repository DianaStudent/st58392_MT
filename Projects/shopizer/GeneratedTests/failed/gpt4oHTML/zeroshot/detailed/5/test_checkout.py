from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Accept cookies if prompt appears
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            cookie_button.click()
        except:
            pass

        # Log in
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.account-setting-active')))
        account_button.click()
        
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_button.click()

        email_field = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
        email_field.send_keys("test22@user.com")
        
        password_field = wait.until(EC.element_to_be_clickable((By.NAME, 'loginPassword')))
        password_field.send_keys("test**11")
        
        login_submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_submit.click()

        # Navigate back to the home page
        home_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Home')))
        home_link.click()

        # Hover over first product and click "Add to cart"
        first_product = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()
        
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, 'button[title="Add to cart"]')
        add_to_cart_button.click()

        # Open cart popup
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-cart')))
        cart_icon.click()

        # Click "View cart" inside the popup
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'View Cart')))
        view_cart_button.click()

        # Proceed to checkout
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Proceed to Checkout')))
        proceed_to_checkout_button.click()

        # Fill in the billing form
        company_input = wait.until(EC.element_to_be_clickable((By.NAME, 'company')))
        company_input.send_keys("Comp1")
        
        address_input = driver.find_element(By.NAME, 'address')
        address_input.send_keys("Street1")
        
        city_input = driver.find_element(By.NAME, 'city')
        city_input.send_keys("Quebec")

        state_dropdown = driver.find_element(By.CSS_SELECTOR, '.billing-select select')
        for option in state_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == "Quebec":
                option.click()
                break

        postal_code_input = driver.find_element(By.NAME, 'postalCode')
        postal_code_input.send_keys("1234")

        phone_input = driver.find_element(By.NAME, 'phone')
        phone_input.send_keys("1234567891")
        
        # Accept terms and conditions
        terms_checkbox = driver.find_element(By.NAME, 'isAgree')
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        # Check if form is filled correctly
        self.assertTrue(company_input.get_attribute('value'), "Comp1")
        self.assertTrue(address_input.get_attribute('value'), "Street1")
        self.assertTrue(city_input.get_attribute('value'), "Quebec")
        self.assertTrue(postal_code_input.get_attribute('value'), "1234")
        self.assertTrue(phone_input.get_attribute('value'), "1234567891")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()