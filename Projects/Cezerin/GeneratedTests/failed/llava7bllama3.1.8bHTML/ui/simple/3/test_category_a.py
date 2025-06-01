from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-link-home')))

        # Check that the header exists and is visible
        self.assertIsNotNone(self.driver.find_element(By.CSS_SELECTOR, 'h1'))
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed())

        # Check that the buttons exist and are visible
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        for button in buttons:
            self.assertIsNotNone(button)
            self.assertTrue(button.is_displayed())

        # Check that the links exist and are visible
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a')))
        for link in links:
            self.assertIsNotNone(link)
            self.assertTrue(link.is_displayed())

        # Check that the form fields exist and are visible
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input')))
        for field in form_fields:
            self.assertIsNotNone(field)
            self.assertTrue(field.is_displayed())

if __name__ == "__main__":
    unittest.main()