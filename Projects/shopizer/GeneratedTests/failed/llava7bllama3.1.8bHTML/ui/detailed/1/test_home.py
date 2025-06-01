from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_webpage_structural_elements(self):
        self.driver.get("http://localhost/")

        # Ensure header is visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "header"))
        )

        # Ensure navigation and footer are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#navigation")
            )
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )

    def test_ui_elements(self):
        self.driver.get("http://localhost/")

        # Ensure input fields and buttons are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#login_form input")
            )
        )
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )

        # Ensure sections are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#login_form .section")
            )
        )

    def test_interaction(self):
        self.driver.get("http://localhost/login")

        # Interact with login form elements
        username_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.NAME, "username")
            )
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.NAME, "password")
            )
        )

        # Click login button
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )
        login_button.click()

    def test_ui_reacts_visually(self):
        self.driver.get("http://localhost/login")

        # Ensure UI reacts visually when clicking buttons
        # (e.g., change in button color or text)

if __name__ == "__main__":
    unittest.main()