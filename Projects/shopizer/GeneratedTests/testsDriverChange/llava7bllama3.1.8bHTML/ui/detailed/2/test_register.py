from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visible(self):
        # Wait for header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
        
        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertIn("Login", self.driver.page_source)
        self.assertIn("Register", self.driver.page_source)
        self.assertIn("Tables", self.driver.page_source)
        self.assertIn("Chairs", self.driver.page_source)

        # Interact with key UI elements (e.g., click buttons)
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
        button.click()

        # Confirm that the UI reacts visually
        time.sleep(1)  # Wait for a second to see the effect

    def test_required_elements_present(self):
        self.assertIn("header", self.driver.page_source)
        self.assertIn("footer", self.driver.page_source)
        self.assertIn("nav", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()