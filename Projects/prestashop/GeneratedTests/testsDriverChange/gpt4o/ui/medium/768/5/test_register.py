import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Confirm the presence of header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertTrue(header.is_displayed(), "Header is not displayed")

        # Confirm the presence of navigation links
        nav_links = [
            (By.XPATH, "//a[@href='http://localhost:8080/en/']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        ]
        for (selector_type, selector) in nav_links:
            element = self.wait.until(EC.visibility_of_element_located((selector_type, selector)))
            self.assertTrue(element.is_displayed(), f"Navigation link {selector} is not displayed")

        # Confirm form fields presence
        form_fields = [
            (By.ID, "field-firstname"),
            (By.ID, "field-lastname"),
            (By.ID, "field-email"),
            (By.ID, "field-password"),
            (By.ID, "field-birthday")
        ]
        for (selector_type, selector) in form_fields:
            element = self.wait.until(EC.visibility_of_element_located((selector_type, selector)))
            self.assertTrue(element.is_displayed(), f"Form field {selector} is not displayed")

        # Confirm presence of buttons
        save_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.assertTrue(save_button.is_displayed(), "Save button is not displayed")

        # Interact with elements
        save_button.click()

        # Verify that interaction does not cause errors
        # Assuming the UI redirects to another page or shows a message
        # Check for a post-click element or message
        try:
            post_click_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'already have an account')]")))
            self.assertTrue(post_click_message.is_displayed(), "Expected message after click not displayed")
        except Exception as e:
            self.fail(f"Post-click UI update failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()