from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check that the header is present
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check that the main navigation links are present
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav .cat-parent a")))
        categories = ["Category A", "Category B", "Category C"]
        for i, link in enumerate(nav_links):
            self.assertIn(categories[i], link.text, f"Navigation link {categories[i]} is not visible")

        # Check that the search box is present
        search_box = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        self.assertIsNotNone(search_box, "Search box is not visible")

        # Check that the sort select is present
        sort_select = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort select")))
        self.assertIsNotNone(sort_select, "Sort select is not visible")

        # Check that the products are displayed
        products = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
        self.assertGreater(len(products), 0, "Products are not visible")

        # Interact with the sort select
        sort_select.click()
        sort_option_newest = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='-date_created']")))
        sort_option_newest.click()

        # Check for UI updates post interaction (e.g., sorted order)
        self.assertEqual(sort_select.get_attribute('value'), '-date_created', "Sort select did not update to newest")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()