import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        try:
            # Header navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))

            # Logo
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo img')))
            self.assertTrue(logo.is_displayed(), "Logo is not displayed")

            # Accept cookies button
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertTrue(cookie_button.is_displayed(), "Accept cookies button is not displayed")

            # Account and Cart buttons
            account_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'account-setting-active')))
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-cart')))
            self.assertTrue(account_button.is_displayed(), "Account button is not displayed")
            self.assertTrue(cart_button.is_displayed(), "Cart button is not displayed")

            # Footer links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))

            # Subscribe form
            email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Subscribe')]")))
            self.assertTrue(email_field.is_displayed(), "Email field is not displayed")
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not displayed")

        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()