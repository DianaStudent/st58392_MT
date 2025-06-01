import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header not found or not visible.")
        
        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer not found or not visible.")
        
        # Check main navigation links
        nav_links = ["http://localhost:8080/en/", "http://localhost:8080/en/3-clothes", 
                     "http://localhost:8080/en/6-accessories", "http://localhost:8080/en/9-art"]
        for link in nav_links:
            nav_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            self.assertIsNotNone(nav_element, f"Navigation link {link} not found or not visible.")
        
        # Check login link
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']")))
        self.assertIsNotNone(login_link, "Login link not found or not visible.")
        
        # Check search input field
        search_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertIsNotNone(search_field, "Search input field not found or not visible.")
        
        # Check that sort by dropdown is present
        sort_by_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-sort-order")))
        self.assertIsNotNone(sort_by_dropdown, "Sort by dropdown not found or not visible.")

        # Check product list
        product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        self.assertIsNotNone(product_list, "Product list not found or not visible.")
        
        # Interact: Click the first product's quick view button
        quick_view_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".quick-view.js-quick-view")))
        quick_view_button.click()

        # Wait for quick view to become visible
        quick_view_modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        self.assertIsNotNone(quick_view_modal, "Quick view modal did not appear.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()