from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        # Wait for 20 seconds before interacting with elements
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    def test_ui_elements(self):
        # Check that structural elements (e.g., header, footer, navigation) are visible
        self.assertEqual(self.driver.find_elements(By.TAG_NAME, "header").__len__, 1)
        self.assertEqual(self.driver.find_elements(By.TAG_NAME, "footer").__len__, 1)
        self.assertEqual(self.driver.find_elements(By.TAG_NAME, "nav").__len__, 1)

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.driver.find_element(By.NAME, "username").is_displayed())
        self.assertTrue(self.driver.find_element(By.NAME, "password").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@type='submit']").is_enabled())

        # Interact with key UI elements (e.g., click buttons)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        # Confirm that the UI reacts visually
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "h1").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()