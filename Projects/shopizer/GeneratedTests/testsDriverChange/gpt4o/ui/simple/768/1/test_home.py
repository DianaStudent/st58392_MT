import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        except Exception as e:
            self.fail(f"Header not found: {e}")

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        except Exception as e:
            self.fail(f"Navigation link(s) not found: {e}")

        # Check cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except Exception as e:
            self.fail(f"Cookie consent button not found: {e}")

        # Check account settings button
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'account-setting-active')))
        except Exception as e:
            self.fail(f"Account settings button not found: {e}")

        # Check cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-cart')))
        except Exception as e:
            self.fail(f"Cart icon not found: {e}")

        # Check main page elements
        try:
            banner_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.site-blocks-cover img')))
            featured_products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'section-title-5')))
        except Exception as e:
            self.fail(f"Main page element(s) not found: {e}")

        # Check subscribe form
        try:
            subscribe_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form input.email')))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form button')))
        except Exception as e:
            self.fail(f"Subscribe form element(s) not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()