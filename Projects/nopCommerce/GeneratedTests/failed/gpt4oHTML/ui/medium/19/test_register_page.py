from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_presence(self):
        driver = self.driver

        # Confirm navigation links are present
        nav_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us"),
        ]

        for link_text, by, value in nav_links:
            with self.subTest(link_text=link_text):
                nav_element = self.wait.until(EC.visibility_of_element_located((by, value)))
                self.assertTrue(nav_element.is_displayed(), f"Navigation link '{link_text}' is not visible")

        # Confirm input fields are present
        input_fields = [
            (By.ID, "FirstName"),
            (By.ID, "LastName"),
            (By.ID, "Email"),
            (By.ID, "Password"),
            (By.ID, "ConfirmPassword"),
        ]

        for field, by, value in input_fields:
            with self.subTest(input_field=field):
                input_element = self.wait.until(EC.visibility_of_element_located((by, value)))
                self.assertTrue(input_element.is_displayed(), f"Input field '{field}' is not visible")

        # Confirm buttons are present
        register_button = self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

        # Interact with elements and check UI behavior
        register_button.click()

        # Check if any UI errors appear, assuming page stays and no redirects or alerts as UI feedback
        self.assertTrue(register_button.is_displayed(), "Register button is not visible after click (possible UI error)")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()