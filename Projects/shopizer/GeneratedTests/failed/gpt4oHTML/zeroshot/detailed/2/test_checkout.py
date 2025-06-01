from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')  # assume local test server

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Open the home page (already done in setUp)
        # Click the 'Login' link
        account_setting_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'account-setting-active')))
        account_setting_button.click()
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_link.click()

        # Log in using provided credentials
        username_input = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
        username_input.send_keys('test22@user.com')

        password_input = driver.find_element(By.NAME, 'loginPassword')
        password_input.send_keys('test**11')

        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        
        # Navigate back to the home page
        home_nav = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Home')))
        home_nav.click()

        # Hover over the first product and click "Add to cart"
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-cart')))
        cart_icon.click()

        # Wait for cart popup to become visible and click "View Cart"
        view_cart_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'View Cart')))
        view_cart_button.click()

        # On the cart page, proceed to checkout
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Proceed to Checkout')))
        proceed_to_checkout_button.click()

        # Fill out the billing form
        wait.until(EC.element_to_be_clickable((By.NAME, 'company'))).send_keys('Comp1')
        driver.find_element(By.NAME, 'address').send_keys('Street1')
        driver.find_element(By.NAME, 'city').send_keys('Quebec')
        
        # Select region/state from dropdown
        state_dropdown = driver.find_element(By.NAME, 'state')
        state_dropdown.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Quebec')]"))).click()
        
        driver.find_element(By.NAME, 'postalCode').send_keys('1234')
        driver.find_element(By.NAME, 'phone').send_keys('1234567891')
        
        # Accept terms and conditions
        terms_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='isAgree']")
        terms_checkbox.click()

        # Verify the billing form is filled
        self.assertTrue(driver.find_element(By.NAME, 'phone').get_attribute('value') == '1234567891')

if __name__ == '__main__':
    unittest.main()