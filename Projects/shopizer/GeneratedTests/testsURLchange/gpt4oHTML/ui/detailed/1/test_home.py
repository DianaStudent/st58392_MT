from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Ensure structural elements like header, footer, and navigation are visible
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        except:
            self.fail("Header area is not visible.")

        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        except:
            self.fail("Footer area is not visible.")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav')))
        except:
            self.fail("Navigation menu is not visible.")

        # Check presence and visibility of input fields, buttons, labels, and sections
        # Accept cookies button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertTrue(cookie_button.is_displayed(), "Cookie button is not visible.")
        except:
            self.fail("Cookie button is not present.")

        # Products section
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-area')))
        except:
            self.fail("Product area is not visible.")

        # Subscribe section
        try:
            subscribe_section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'subscribe-area-3')))
            self.assertTrue(subscribe_section.is_displayed(), "Subscribe section is not visible.")
        except:
            self.fail("Subscribe section is not present.")

        # Interact with key UI elements, e.g., click a button
        try:
            cookie_button.click()
            # Confirm that the UI reacts visually by checking that the cookie banner disappears
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'CookieConsent')))
        except:
            self.fail("Cookie consent not dismissed after clicking accept.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()