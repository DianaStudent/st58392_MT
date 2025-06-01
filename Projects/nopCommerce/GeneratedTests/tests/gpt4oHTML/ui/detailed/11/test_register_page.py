import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StoreUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://max/register?returnUrl=%2F")

        # Wait for and check header
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'header'))
        )
        self.assertIsNotNone(header, "Header is not present or visible")

        # Wait for and check footer
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'footer'))
        )
        self.assertIsNotNone(footer, "Footer is not present or visible")

        # Check presence and visibility of form fields on registration page
        form_fields = ['FirstName', 'LastName', 'Email', 'Password', 'ConfirmPassword']
        for field_id in form_fields:
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            self.assertIsNotNone(element, f"{field_id} field is not present or visible")

        # Check all main buttons
        main_buttons = ['register-button']
        for button_id in main_buttons:
            button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, button_id))
            )
            self.assertIsNotNone(button, f"{button_id} is not present or visible")

        # Check for Register and Login links in the header
        register_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ico-register'))
        )
        self.assertIsNotNone(register_link, "Register link is not present or visible")

        login_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ico-login'))
        )
        self.assertIsNotNone(login_link, "Login link is not present or visible")

        # Interact with the Newsletter checkbox
        newsletter_checkbox = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'Newsletter'))
        )
        self.assertIsNotNone(newsletter_checkbox, "Newsletter checkbox is not present or visible")
        newsletter_checkbox.click()

        # Confirm button click action changes
        register_button = driver.find_element(By.ID, 'register-button')
        register_button.click()
        WebDriverWait(driver, 20).until(
            EC.url_contains("/register")
        )

        # Confirm no required element is missing
        required_elements = [header, footer, register_link, login_link, newsletter_checkbox]
        for element in required_elements:
            self.assertIsNotNone(element, "A required UI element is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()