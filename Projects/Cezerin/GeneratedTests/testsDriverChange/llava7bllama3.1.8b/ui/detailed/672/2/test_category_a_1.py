import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:3000')

    def test_main_page_elements(self):
        # Check header elements
        self.assertTrue(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        header_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        self.assertEqual(header_title.text, '')

        # Check navigation bar
        self.assertTrue(EC.presence_of_element_located((By.TAG_NAME, 'nav')))

        # Check footer elements
        self.assertTrue(EC.presence_of_element_located((By.TAG_NAME, 'footer')))
        footer_logo = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#logo')))
        self.assertEqual(footer_logo.get_attribute('src'), '/assets/img/logo.png')

    def test_category_a_page_elements(self):
        # Navigate to category-a page
        self.driver.get('http://localhost:3000/category-a')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))

        # Check category-a header elements
        category_a_header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.category-header')))
        self.assertEqual(category_a_header.text, '')

        # Check navigation bar
        self.assertTrue(EC.presence_of_element_located((By.TAG_NAME, 'nav')))

    def test_category_a_1_page_elements(self):
        # Navigate to category-a-1 page
        self.driver.get('http://localhost:3000/category-a-1')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))

        # Check category-a-1 header elements
        category_a_1_header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.category-header')))
        self.assertEqual(category_a_1_header.text, '')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()