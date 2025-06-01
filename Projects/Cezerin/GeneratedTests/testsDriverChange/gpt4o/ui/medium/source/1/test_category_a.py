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
        self.wait = WebDriverWait(self.driver, 20)
        self.home_url = "http://localhost:3000"

    def tearDown(self):
        self.driver.quit()

    def test_category_a_page_elements(self):
        self.driver.get(f"{self.home_url}/category-a")

        # Check and validate the main navigation links are present and visible
        nav_links = ["Category A", "Category B", "Category C"]
        for link_text in nav_links:
            link_elem = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, link_text))
            )
            self.assertIsNotNone(link_elem)
        
        # Check Search input box
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-input"))
        )
        self.assertIsNotNone(search_input)
        
        # Check for category title
        category_title = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "category-title"))
        )
        self.assertEqual(category_title.text, "Category A")
        
        # Check sort dropdown
        sort_dropdown = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sort"))
        )
        self.assertIsNotNone(sort_dropdown)
        
        # Check existence of product links
        product_links = self.driver.find_elements(By.CSS_SELECTOR, ".products a")
        self.assertGreaterEqual(len(product_links), 2)

        # Interact with an element: Click on "Product A"
        product_a = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Product A"))
        )
        product_a.click()

        # Verify page URL updated to Product A URL
        self.wait.until(lambda driver: driver.current_url == f"{self.home_url}/category-a/product-a")

        # Ensure no visible errors after interaction
        self.assertTrue(self.driver.title)

if __name__ == "__main__":
    unittest.main()