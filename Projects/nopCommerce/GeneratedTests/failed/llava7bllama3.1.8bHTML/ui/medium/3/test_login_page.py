from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_ui_elements(self):
        # Check navigation links presence
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//nav//a")))
        for link in nav_links:
            self.assertTrue(link.is_displayed())

        # Check input fields presence
        inputs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='text']")))
        for inp in inputs:
            self.assertTrue(inp.is_enabled())
            self.assertTrue(inp.is_displayed())

        # Click button and verify UI update
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='newsletter-subscribe-button']")))
        button.click()
        self.assertEqual(button.text, "Subscribe")

    def test_no_errors_on_interactive_elements(self):
        # Check buttons and links do not cause errors
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='newsletter-subscribe-button']")))
        button.click()
        self.assertTrue(button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()