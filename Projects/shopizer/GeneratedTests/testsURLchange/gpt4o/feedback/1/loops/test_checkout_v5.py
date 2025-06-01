import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        self.click_element(By.ID, 'rcc-confirm-button')

        # Click on the login button
        self.click_element(By.CSS_SELECTOR, 'button.account-setting-active')
        self.click_element(By.LINK_TEXT, 'Login')

        # Enter login credentials and submit
        driver.find_element(By.NAME, 'username').send_keys("test22@user.com")
        driver.find_element(By.NAME, 'loginPassword').send_keys("test**11")
        login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.login-register-form button')))
        login_btn.click()

        # Check for successful login
        welcome_user = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-name')))
        self.assertIn("Welcome Test User", welcome_user.text)

        # Navigate back to the home page
        driver.get("http://localhost/")

        # Hover over the first product to show "Add to cart" button
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()

        # Click "Add to cart"
        self.click_element(By.CSS_SELECTOR, '.fa-shopping-cart')

        # Click on cart icon to open popup cart
        self.click_element(By.CSS_SELECTOR, 'button.icon-cart')

        # Click "View Cart" button
        self.click_element(By.LINK_TEXT, 'View Cart')

        # On the cart page, click "Proceed to Checkout"
        self.click_element(By.LINK_TEXT, 'Proceed to Checkout')

        # Fill out the billing form
        driver.find_element(By.NAME, 'firstName').send_keys("First")
        driver.find_element(By.NAME, 'lastName').send_keys("Last")
        driver.find_element(By.NAME, 'company').send_keys("Comp1")
        driver.find_element(By.NAME, 'address').send_keys("Street1")
        driver.find_element(By.NAME, 'city').send_keys("Quebec")

        # Select region/state from dropdown
        Select(driver.find_element(By.NAME, 'state')).select_by_visible_text("Quebec")

        driver.find_element(By.NAME, 'postalCode').send_keys("1234")
        driver.find_element(By.NAME, 'phone').send_keys("1234567891")

        # Accept terms and conditions
        self.click_element(By.NAME, 'isAgree')

        # Assert form entries to confirm success
        self.assertEqual(driver.find_element(By.NAME, 'company').get_attribute('value'), "Comp1")
        self.assertEqual(driver.find_element(By.NAME, 'address').get_attribute('value'), "Street1")
        self.assertEqual(driver.find_element(By.NAME, 'city').get_attribute('value'), "Quebec")
        self.assertEqual(driver.find_element(By.NAME, 'postalCode').get_attribute('value'), "1234")
        self.assertEqual(driver.find_element(By.NAME, 'phone').get_attribute('value'), "1234567891")

    def click_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            element.click()
        except Exception as e:
            self.fail(f"Element with locator {by}={value} is not found. Error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()