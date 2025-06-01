from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_page_structure(self):
        # Check that structural elements are visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#block_top_menu")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header")))

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, "input"))
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, "button"))
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, "label"))

        # Interact with key UI elements (e.g., click buttons)
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart")))
        button.click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ajax_block_add")))

        # Assert that no required UI element is missing
        self.assertFalse(self.driver.find_elements(By.TAG_NAME, "div") == [])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()