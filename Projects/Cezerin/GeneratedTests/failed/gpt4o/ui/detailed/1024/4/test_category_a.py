from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get("http://localhost:3000/category-a")
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check main navigation
        primary_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav")))
        self.assertIsNotNone(primary_nav, "Primary navigation is not visible")

        # Check search input field visibility
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        self.assertIsNotNone(search_input, "Search input field is not visible")

        # Check 'Category A' link visibility
        category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
        self.assertIsNotNone(category_a_link, "'Category A' link is not visible")

        # Check product sorting select element
        sort_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
        self.assertIsNotNone(sort_select, "Sort select element is not visible")

        # Check Product A presence
        product_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product A")))
        self.assertIsNotNone(product_a, "Product A is not visible")

        # Check Product B presence
        product_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product B")))
        self.assertIsNotNone(product_b, "Product B is not visible")

        # Interact with Product A
        product_a.click()
        product_a_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-name")))
        self.assertIn("Product A", product_a_name.text, "Failed to load Product A details")

if __name__ == "__main__":
    unittest.main()