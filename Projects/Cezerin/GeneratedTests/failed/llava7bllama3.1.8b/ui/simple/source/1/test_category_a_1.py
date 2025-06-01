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
        self.driver.get('http://localhost:3000')

    def tearDown(self):
        self.driver.quit()

    def test_main_components(self):
        # Wait for the main UI components to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'main-content')))

        # Check that required elements are present in the header
        self.assertTrue(self.driver.find_element(By.TAG_NAME, 'h1').text == 'Header')
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, 'button'))

        # Check that required elements are present in the main content area
        self.assertTrue(self.driver.find_element(By.ID, 'product-list'))
        self.assertTrue(self.driver.find_element(By.ID, 'search-bar'))

    def test_category_a_links(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
        category_a_link = self.driver.find_element(By.LINK_TEXT, 'Category A')
        category_a_link.click()

        # Wait for the Category A page to be loaded
        WebDriverWait(self.driver, 20).until(EC.url_contains('category-a'))

        # Check that required elements are present on the Category A page
        self.assertTrue(self.driver.find_element(By.ID, 'category-a-content'))
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, 'h2'))

    def test_category_a_1_links(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A 1')))
        category_a_1_link = self.driver.find_element(By.LINK_TEXT, 'Category A 1')
        category_a_1_link.click()

        # Wait for the Category A 1 page to be loaded
        WebDriverWait(self.driver, 20).until(EC.url_contains('category-a-1'))

        # Check that required elements are present on the Category A 1 page
        self.assertTrue(self.driver.find_element(By.ID, 'category-a-1-content'))
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, 'h2'))

if __name__ == '__main__':
    unittest.main()