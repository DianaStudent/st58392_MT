from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # Log in
        account_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()
        
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        username_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
        
        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")

        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']")))
        login_button.click()

        # Navigate back to the home page
        driver.get("http://localhost/")

        # Hover over the first product
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        ActionChains(driver).move_to_element(first_product).perform()

        # Click "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Click "View Cart" button in the popup
        view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # On the cart page, click "Proceed to Checkout"
        proceed_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill out the billing form
        self.wait.until(EC.element_to_be_clickable((By.NAME, "firstName"))).send_keys("Comp1")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "address"))).send_keys("Street1")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "city"))).send_keys("Quebec")

        country_select = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='country']")))
        country_select.send_keys("Canada")
        
        province_select = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[name='region']")))
        province_select.send_keys("Quebec")
        
        self.wait.until(EC.element_to_be_clickable((By.NAME, "postalCode"))).send_keys("1234")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "phone"))).send_keys("1234567891")

        # Accept terms checkbox
        terms_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "isAgree")))
        terms_checkbox.click()

        # Ensure the billing form is filled
        filled_company = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).get_attribute('value')
        if filled_company != "Comp1":
            self.fail("The billing form is not filled correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()