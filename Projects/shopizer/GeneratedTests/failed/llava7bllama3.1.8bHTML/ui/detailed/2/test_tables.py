from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_page_elements(self):
        # Navigate to the page
        url_home = "http://localhost/"
        self.driver.get(url_home)

        # Wait for elements to be visible on the home page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        )

        # Check presence and visibility of input fields, buttons, labels, sections etc.
        self.assertTrue(self.is_visible(By.XPATH, "//input[@name='search']"))
        self.assertTrue(self.is_visible(By.XPATH, "//button[@type='submit']"))
        self.assertTrue(self.is_visible(By.XPATH, "//h1[@class='page-title']"))

        # Interact with key UI elements (e.g., click buttons)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category/tables']"))
        ).click()
        self.assertTrue(self.is_visible(By.XPATH, "//h2[@class='page-title']"))

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        )

        # Assert that no required UI element is missing
        self.assertTrue(self.is_visible(By.XPATH, "//header"))
        self.assertTrue(self.is_visible(By.XPATH, "//footer"))

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

if __name__ == '__main__':
    unittest.main()