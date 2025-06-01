import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertIsNotNone(header, "Header is missing or not visible.")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertIsNotNone(footer, "Footer is missing or not visible.")

        # Check main menu
        main_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav ul')))
        self.assertIsNotNone(main_menu, "Main menu is missing or not visible.")

        # Check Login and Register navigation
        login_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/login"]')))
        self.assertIsNotNone(login_link, "Login link is missing or not visible.")

        register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/register"]')))
        self.assertIsNotNone(register_link, "Register link is missing or not visible.")

        # Check input fields on the login page
        login_link.click()
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        self.assertIsNotNone(username_input, "Username input field is missing or not visible.")

        password_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-password')))
        self.assertIsNotNone(password_input, "Password input field is missing or not visible.")

        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        self.assertIsNotNone(login_button, "Login button is missing or not visible.")

        # Check structural cookie consent
        cookie_consent = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertIsNotNone(cookie_consent, "Cookie consent button is missing or not visible.")
        cookie_consent.click()

        # Interact with login button to check UI reaction
        login_button.click()
        # Wait for some response or change in the UI, add specific responses that you expect on the UI

        # Additional interactions and assertions can be added here as needed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()