import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify presence and visibility of the navigation links
        try:
            nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.nav-level-0 a")))
            self.assertTrue(len(nav_links) > 0, "Navigation links are not visible")
        except Exception as e:
            self.fail(f"Navigation links are missing: {str(e)}")

        # Verify presence and visibility of the search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        except Exception as e:
            self.fail(f"Search input is missing: {str(e)}")

        # Verify presence and visibility of the sort select
        try:
            sort_select = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
            self.assertTrue(sort_select.is_displayed(), "Sort select is not visible")
        except Exception as e:
            self.fail(f"Sort select is missing: {str(e)}")

        # Verify presence and visibility of product links and click one
        try:
            product_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products a")))
            self.assertTrue(len(product_links) > 0, "Product links are not visible")
            product_links[0].click()
        except Exception as e:
            self.fail(f"Product links are missing or clickable: {str(e)}")

        # Wait to ensure no UI errors after clicking
        try:
            self.wait.until(EC.url_contains("/product"))  # Simplest way to confirm UI updates
        except Exception as e:
            self.fail(f"UI did not update correctly after clicking product: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()