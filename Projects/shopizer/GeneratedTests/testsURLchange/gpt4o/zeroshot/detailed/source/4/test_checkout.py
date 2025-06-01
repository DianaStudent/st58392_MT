import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        cookie_button = self.wait.until(EC.presence_of_element_located((By.ID, 'rcc-confirm-button')))
        if not cookie_button.text.strip():
            self.fail("Cookie button not found or not visible")
        cookie_button.click()

        # Log in
        account_setting = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.account-setting-active')))
        ActionChains(driver).move_to_element(account_setting).click().perform()
        
        login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        if not login_link.text.strip():
            self.fail("Login link not found or not visible")
        login_link.click()

        username = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        password = driver.find_element(By.NAME, 'loginPassword')
        username.send_keys('test22@user.com')
        password.send_keys('test**11')

        login_button = driver.find_element(By.CSS_SELECTOR, '.button-box button')
        if not login_button.text.strip():
            self.fail("Login button not found or not visible")
        login_button.click()

        # Navigate back to home page
        driver.find_element(By.CSS_SELECTOR, '.logo a').click()

        # Hover over first product and add to cart
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()
        
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, 'button[title="Add to cart"]')
        if not add_to_cart_button.get_attribute('title').strip():
            self.fail("Add to cart button not found or not visible")
        add_to_cart_button.click()

        # Open cart and proceed to checkout
        cart_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.icon-cart')))
        ActionChains(driver).move_to_element(cart_icon).click().perform()

        view_cart_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'View Cart')))
        if not view_cart_button.text.strip():
            self.fail("View Cart button not found or not visible")
        view_cart_button.click()

        proceed_to_checkout = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Proceed to Checkout')))
        if not proceed_to_checkout.text.strip():
            self.fail("Proceed to Checkout button not found or not visible")
        proceed_to_checkout.click()

        # Fill billing form
        billing_details = {
            'company': 'Comp1',
            'address': 'Street1',
            'city': 'Quebec',
            'postalCode': '1234',
            'phone': '1234567891'
        }

        for key, value in billing_details.items():
            element = self.wait.until(EC.presence_of_element_located((By.NAME, key)))
            element.clear()
            if not element.get_attribute('placeholder').strip():
                self.fail(f"{key} input not found or not visible")
            element.send_keys(value)

        # Select region/state
        state_select = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select')))
        for option in state_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'Quebec':
                option.click()
                break

        # Accept terms and place the order
        terms_agree = self.wait.until(EC.presence_of_element_located((By.NAME, 'isAgree')))
        terms_agree.click()

        # Assume any map or warning popups have a specific CSS selector
        # map_popup_close = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.map-popup-close')))
        # map_popup_close.click()
        
        form_elements = driver.find_elements(By.CSS_SELECTOR, 'input, select')
        for element in form_elements:
            if not element.get_attribute('value') and element.is_displayed():
                self.fail("Billing form is not completely filled")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()