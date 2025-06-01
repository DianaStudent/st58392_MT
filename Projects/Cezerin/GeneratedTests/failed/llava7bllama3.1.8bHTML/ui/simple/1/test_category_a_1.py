from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://your-url.com')  # Replace with your URL

    def test_main_ui_components_present(self):
        # Check headers
        headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h1')))
        for header in headers:
            self.assertTrue(header.is_displayed())

        # Check buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Check links
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a')))
        for link in links:
            self.assertTrue(link.is_displayed())

        # Check form fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input')))
        for field in form_fields:
            self.assertTrue(field.is_displayed())

    def test_category_a_link_present(self):
        category_a_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'category_a')))
        self.assertTrue(category_a_link.is_enabled())
        self.assertTrue(category_a_link.is_displayed())

    def test_category_a_1_link_present(self):
        category_a_1_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'category_a_1')))
        self.assertTrue(category_a_1_link.is_enabled())
        self.assertTrue(category_a_1_link.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()