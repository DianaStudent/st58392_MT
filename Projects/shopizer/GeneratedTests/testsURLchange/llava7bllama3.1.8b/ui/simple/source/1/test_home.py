from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import os

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_main_page_components(self):
        # Go to main page
        self.driver.get('http://localhost/')

        # Wait for elements to be visible and assert they exist
        headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h1')))
        self.assertGreater(len(headers), 0)

        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        self.assertGreater(len(buttons), 0)

        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a')))
        self.assertGreater(len(links), 0)

    def test_tables_category_components(self):
        # Go to tables category page
        self.driver.get('http://localhost/category/tables')

        # Wait for elements to be visible and assert they exist
        headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h1')))
        self.assertGreater(len(headers), 0)

        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        self.assertGreater(len(buttons), 0)

    def test_chairs_category_components(self):
        # Go to chairs category page
        self.driver.get('http://localhost/category/chairs')

        # Wait for elements to be visible and assert they exist
        headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h1')))
        self.assertGreater(len(headers), 0)

        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        self.assertGreater(len(buttons), 0)

    def test_login_components(self):
        # Go to login page
        self.driver.get('http://localhost/login')

        # Wait for elements to be visible and assert they exist
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input')))
        self.assertGreater(len(form_fields), 0)

    def test_register_components(self):
        # Go to register page
        self.driver.get('http://localhost/register')

        # Wait for elements to be visible and assert they exist
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input')))
        self.assertGreater(len(form_fields), 0)

if __name__ == '__main__':
    unittest.main()