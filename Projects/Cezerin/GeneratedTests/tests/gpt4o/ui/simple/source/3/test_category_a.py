import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except Exception:
            self.fail("Header is not visible")

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image")))
        except Exception:
            self.fail("Logo is not visible")

        # Check search bar
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        except Exception:
            self.fail("Search bar is not visible")

        # Check cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button .icon")))
        except Exception:
            self.fail("Cart icon is not visible")

        # Check category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".category-title")))
        except Exception:
            self.fail("Category title is not visible")

        # Check product links
        try:
            product_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .product-caption")))
            if len(product_links) < 2:
                self.fail("Less than 2 products visible")
        except Exception:
            self.fail("Product links are not visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except Exception:
            self.fail("Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()