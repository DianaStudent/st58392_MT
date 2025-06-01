import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait
        
        # Header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            nav_links = header.find_elements(By.CSS_SELECTOR, ".primary-nav a")
            self.assertTrue(len(nav_links) > 0, "Navigation links in the header are missing.")
        except Exception as e:
            self.fail(f"Header check failed: {str(e)}")
        
        # Footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            company_links = footer.find_elements(By.CSS_SELECTOR, ".footer-menu a")
            self.assertTrue(len(company_links) > 0, "Footer links are missing.")
        except Exception as e:
            self.fail(f"Footer check failed: {str(e)}")
        
        # Search input
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
            self.assertTrue(search_box.is_displayed(), "Search input field is missing.")
        except Exception as e:
            self.fail(f"Search input field check failed: {str(e)}")
        
        # Category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
            self.assertTrue(category_title.is_displayed(), "Category title is missing.")
        except Exception as e:
            self.fail(f"Category title check failed: {str(e)}")
        
        # Product elements
        try:
            products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .column")))
            self.assertTrue(len(products) > 0, "Product elements are missing.")
        except Exception as e:
            self.fail(f"Product elements check failed: {str(e)}")
        
        # Click and verify interaction
        try:
            products[0].click()
            # Verify the click led to a new page or UI change
            product_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-name")))
            self.assertTrue(product_name.is_displayed(), "Product detail view is not displayed after clicking a product.")
        except Exception as e:
            self.fail(f"Interaction check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()