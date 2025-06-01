import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header should be present and visible")

        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer should be present and visible")

        # Verify navigation links are visible
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        # Check login form fields
        email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))

        # Check login and register buttons
        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

        # Interact with UI elements
        login_button.click()

        # Assert all UI elements are as expected
        self.assertTrue(home_link.is_displayed(), "Home link should be visible")
        self.assertTrue(tables_link.is_displayed(), "Tables link should be visible")
        self.assertTrue(chairs_link.is_displayed(), "Chairs link should be visible")
        self.assertTrue(email_field.is_displayed(), "Email field should be visible")
        self.assertTrue(password_field.is_displayed(), "Password field should be visible")
        self.assertTrue(login_button.is_displayed(), "Login button should be visible")
        self.assertTrue(register_link.is_displayed(), "Register link should be visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()