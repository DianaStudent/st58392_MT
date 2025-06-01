import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        # Navigate to the login page
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Wait for 20 seconds before interacting with elements
        wait = WebDriverWait(self.driver, 20)

        # Check that the main UI components are present and visible
        self.check_element_present(wait, By.XPATH, "//input[@name='email']")
        self.check_element_present(wait, By.XPATH, "//input[@name='password']")
        self.check_element_present(wait, By.XPATH, "//button[text()='Log in']")

    def check_element_present(self, wait, by_type, locator):
        element = wait.until(EC.element_to_be_clickable((by_type, locator)))
        if not element.is_displayed():
            self.fail(f"Element {locator} is not visible")
        return True

if __name__ == "__main__":
    unittest.main()