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

    def test_UI_elements(self):
        driver = self.driver

        # Check header is visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible")

        # Check navigation links are visible
        try:
            nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav a')))
        except:
            self.fail("Navigation links are not visible")

        # Check if search input is visible
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        except:
            self.fail("Search input is not visible")

        # Check category title is visible
        try:
            category_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.category-title')))
        except:
            self.fail("Category title is not visible")

        # Check product links are visible
        try:
            product_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.product-caption .product-name')))
        except:
            self.fail("Product links are not visible")

        # Check footer is visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is not visible")

        # Interacting with key UI elements
        try:
            sort_dropdown = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sort select')))
            sort_dropdown.click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sort select option[value="price"]'))).click()
        except:
            self.fail("Unable to interact with sort dropdown")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()