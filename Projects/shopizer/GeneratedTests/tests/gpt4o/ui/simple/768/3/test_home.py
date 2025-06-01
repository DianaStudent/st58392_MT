import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestWebElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-area')))
        except:
            self.fail("Header not found or not visible.")

        # Verify main menu links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        except:
            self.fail("Main menu links not found or not visible.")

        # Verify account setting button
        try:
            account_setting_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.account-setting-active')))
        except:
            self.fail("Account setting button not found or not visible.")

        # Verify cart icon
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.icon-cart')))
        except:
            self.fail("Cart icon not found or not visible.")

        # Verify subscription form
        try:
            subscribe_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.email')))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form button')))
        except:
            self.fail("Subscription form elements not found or not visible.")

    def tearDown(self):
        # Quit the driver
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()