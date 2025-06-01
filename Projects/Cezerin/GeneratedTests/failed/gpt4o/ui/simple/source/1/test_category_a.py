from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_are_present(self):
        driver = self.driver
        
        # Verify presence of header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if header is None:
            self.fail("Header not found")

        # Verify presence of main navigation bar
        main_nav = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
        if main_nav is None:
            self.fail("Main navigation bar not found")

        # Verify presence of category title
        category_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.category-title')))
        if category_title is None:
            self.fail("Category title not found")

        # Verify presence of product list
        products = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.columns.is-multiline.products')))
        if products is None:
            self.fail("Product list not found")

        # Verify presence of sort dropdown
        sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        if sort_dropdown is None:
            self.fail("Sort dropdown not found")

        # Verify presence of filter section
        filter_section = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.attribute-filter')))
        if filter_section is None:
            self.fail("Filter section not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()