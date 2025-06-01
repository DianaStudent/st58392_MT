import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify presence of main UI components
        try:
            header = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'header-area'))
            )
            footer = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area'))
            )
            self.assertIsNotNone(header)
            self.assertIsNotNone(footer)
        except Exception as e:
            self.fail("Main UI components are missing: " + str(e))
        
        # Verify presence and functionality of navigation links
        try:
            nav_links = driver.find_elements(By.CSS_SELECTOR, '.main-menu nav ul li a')
            self.assertGreater(len(nav_links), 0, "No navigation links found")

            # Click 'Tables' link and verify it leads to the correct page
            tables_link = driver.find_element(By.LINK_TEXT, 'Tables')
            tables_link.click()
            
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.shop-area'))
            )
            current_url = driver.current_url
            self.assertIn("tables", current_url, "Tables link did not navigate correctly")

            # Go back to the home page
            driver.back()
        except Exception as e:
            self.fail("Navigation links verification failed: " + str(e))
        
        # Verify functionality of a button
        try:
            # Accept cookies button
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            )
            accept_cookies_btn.click()

            # Check that the button is no longer visible after clicking
            self.assertFalse(accept_cookies_btn.is_displayed(), "Accept cookies button still visible after clicking")
        except Exception as e:
            self.fail("Button interaction failed: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()