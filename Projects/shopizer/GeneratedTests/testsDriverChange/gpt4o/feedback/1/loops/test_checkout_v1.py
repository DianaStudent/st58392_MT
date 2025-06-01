import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        wait.until(EC.presence_of_element_located((By.ID, 'rcc-confirm-button'))).click()

        # Click on the login button
        account_setting_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.account-setting-active')))
        account_setting_btn.click()
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_link.click()

        # Assert login page is open
        login_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.login-register-form button')))
        self.assertIsNotNone(login_btn, "Login button does not exist.")

        # Enter login credentials and submit
        driver.find_element(By.NAME, 'username').send_keys("test22@user.com")
        driver.find_element(By.NAME, 'loginPassword').send_keys("test**11")
        login_btn.click()

        # Check for successful login by confirming "Welcome Test User" is present
        welcome_user = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-name')))
        self.assertIn("Welcome Test User", welcome_user.text)

        # Navigate back to the home page
        driver.get("http://localhost/")

        # Hover over the first product to show "Add to cart" button
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()

        # Click "Add to cart"
        add_to_cart_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa-shopping-cart')))
        add_to_cart_btn.click()

        # Click on cart icon to open popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.icon-cart')))
        cart_icon.click()

        # Wait for the popup cart to become visible
        view_cart_btn = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'View Cart')))
        view_cart_btn.click()

        # On the cart page, click "Proceed to Checkout"
        proceed_to_checkout = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Proceed to Checkout')))
        proceed_to_checkout.click()

        # Fill out the billing form
        driver.find_element(By.NAME, 'company').send_keys("Comp1")
        driver.find_element(By.NAME, 'address').send_keys("Street1")
        driver.find_element(By.NAME, 'city').send_keys("Quebec")

        # Select region/state from dropdown
        Select(driver.find_element(By.NAME, 'region')).select_by_visible_text("Quebec")

        driver.find_element(By.NAME, 'postalCode').send_keys("1234")
        driver.find_element(By.NAME, 'phone').send_keys("1234567891")

        # Accept terms and conditions
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, 'isAgree')))
        terms_checkbox.click()
        
        # Assert form entries to confirm success
        self.assertEqual(driver.find_element(By.NAME, 'company').get_attribute('value'), "Comp1")
        self.assertEqual(driver.find_element(By.NAME, 'address').get_attribute('value'), "Street1")
        self.assertEqual(driver.find_element(By.NAME, 'city').get_attribute('value'), "Quebec")
        self.assertEqual(driver.find_element(By.NAME, 'postalCode').get_attribute('value'), "1234")
        self.assertEqual(driver.find_element(By.NAME, 'phone').get_attribute('value'), "1234567891")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()