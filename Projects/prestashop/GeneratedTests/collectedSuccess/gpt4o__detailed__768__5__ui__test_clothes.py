import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Header
            wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Navigation
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-nav")))

            # Footer
            wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Product list header
            wait.until(EC.visibility_of_element_located((By.ID, "js-product-list-header")))

            # Product list
            wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))

            # Main elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-cover")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "subcategory-heading")))

            # Search input
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertIsNotNone(search_input)

            # Sort dropdown
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-sort-order")))
            self.assertIsNotNone(sort_dropdown)

            # First product
            first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-miniature")))
            self.assertIsNotNone(first_product)

            # Wishlist button
            wishlist_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-button-add")))
            self.assertIsNotNone(wishlist_button)

            # Action: Perform a click on the first product
            first_product.find_element(By.TAG_NAME, "a").click()

            # Verify reaction (e.g., page load after clicking product link)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-description")))

        except Exception as e:
            self.fail(f"A required UI element is missing or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()