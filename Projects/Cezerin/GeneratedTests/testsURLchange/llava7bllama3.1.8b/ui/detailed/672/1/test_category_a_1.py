import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")

    def test_category_page_elements(self):
        # Header and Footer Elements
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))

        # Search Bar
        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'search-bar')))

        # Category List
        category_list = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'category-item')))

        # Main Title and Text Block
        main_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        text_block = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))

        # Add Button
        add_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'add-button')))

        # Check if all required elements are present and visible
        self.assertIsNotNone(header)
        self.assertIsNotNone(footer)
        self.assertIsNotNone(search_bar)
        self.assertGreater(len(category_list), 0)
        self.assertIsNotNone(main_title)
        self.assertIsNotNone(text_block)
        self.assertIsNotNone(add_button)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()