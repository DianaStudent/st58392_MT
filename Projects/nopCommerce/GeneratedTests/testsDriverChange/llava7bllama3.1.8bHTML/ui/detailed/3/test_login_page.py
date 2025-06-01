from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMax(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_max(self):
        # Load the page and ensure that structural elements are visible
        self.driver.get('http://max/')

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header')))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer')))

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="search"]'))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))))

        # Interact with key UI elements (e.g., click buttons)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

        # Confirm that the UI reacts visually
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search-result'))))

        # Assert that no required UI element is missing
        expected_elements = ['header', 'input[name="search"]', 'button[type="submit"]']
        for element in expected_elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            except TimeoutException:
                self.fail(f'Element {element} is missing')

if __name__ == '__main__':
    unittest.main()