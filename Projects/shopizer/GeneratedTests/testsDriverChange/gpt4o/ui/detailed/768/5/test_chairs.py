import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is missing")

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check menu items visibility
        menu_items = ["Home", "Tables", "Chairs"]
        for item in menu_items:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, item)))
            self.assertIsNotNone(link, f"Menu item '{item}' is missing")

        # Check buttons visibility
        accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(accept_cookies_button, "Accept cookies button is missing")

        # Interact with UI elements and confirm visual reactions
        accept_cookies_button.click()

        # Check input fields and other form elements
        subscribe_email_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .email")))
        self.assertIsNotNone(subscribe_email_input, "Subscribe email input is missing")

        subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .button")))
        self.assertIsNotNone(subscribe_button, "Subscribe button is missing")

        # Check account links
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertIsNotNone(login_link, "Login link is missing")

        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link, "Register link is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()