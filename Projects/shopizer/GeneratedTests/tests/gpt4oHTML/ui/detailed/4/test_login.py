import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check structural elements
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "main-menu")))
        except:
            self.fail("Essential structural elements are missing or not visible")

        # Check the presence and visibility of input fields, buttons, labels, and sections
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='loginPassword']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".CookieConsent")))
        except:
            self.fail("One or more expected input fields or buttons are missing or not visible")

        # Interact with key UI elements and confirm UI reaction
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()

            # Check that CookieConsent is no longer displayed after clicking Accept
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".CookieConsent")))
        except:
            self.fail("UI did not react as expected after interacting with elements")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()