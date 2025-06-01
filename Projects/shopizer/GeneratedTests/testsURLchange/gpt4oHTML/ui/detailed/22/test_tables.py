import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Check header visibility
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
            self.assertIsNotNone(header, "Header not found or is not visible.")
        except:
            self.fail("Header check failed.")

        # Check footer visibility
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
            self.assertIsNotNone(footer, "Footer not found or is not visible.")
        except:
            self.fail("Footer check failed.")

        # Check navigation links
        try:
            nav_home = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            nav_tables = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            nav_chairs = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
            self.assertTrue(nav_home.is_displayed(), "Home link not visible.")
            self.assertTrue(nav_tables.is_displayed(), "Tables link not visible.")
            self.assertTrue(nav_chairs.is_displayed(), "Chairs link not visible.")
        except:
            self.fail("Navigation links check failed.")

        # Check buttons
        try:
            accept_cookies_btn = self.wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            self.assertTrue(accept_cookies_btn.is_displayed(), "Accept cookies button not visible.")
        except:
            self.fail("Accept cookies button check failed.")

        # Interact with elements
        try:
            accept_cookies_btn.click()
        except:
            self.fail("Failed to click Accept cookies button.")

        # Check input fields and form functionality
        try:
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
            self.assertTrue(subscribe_input.is_displayed(), "Subscribe email input not visible.")
            
            subscribe_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button')))
            self.assertTrue(subscribe_btn.is_displayed(), "Subscribe button not visible.")
        except:
            self.fail("Subscribe form check failed.")

        # Assert main UI components presence
        try:
            header = self.driver.find_element(By.CLASS_NAME, 'header-area')
            footer = self.driver.find_element(By.CLASS_NAME, 'footer-area')
            self.assertIsNotNone(header, "Header is missing.")
            self.assertIsNotNone(footer, "Footer is missing.")
        except:
            self.fail("Main UI components check failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()