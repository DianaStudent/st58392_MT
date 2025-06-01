import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header not visible")

        # Verify navigation links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links not visible")

        # Verify login form
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit'] span")))
        except:
            self.fail("Login form elements not visible")

        # Click the accept cookies button
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except:
            self.fail("Accept cookies button not clickable")

        # Check the footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer not visible")

        # Verify footer elements
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Footer links not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()