from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header visibility
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header, "Header is missing")

            # Check footer visibility
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertIsNotNone(footer, "Footer is missing")

            # Check primary navigation visibility
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "primary-nav")))
            self.assertIsNotNone(nav, "Primary navigation is missing")

            # Check search box visibility
            search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box")))
            self.assertIsNotNone(search_box, "Search box is missing")

            # Check category title visibility
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
            self.assertIsNotNone(category_title, "Category title is missing")

            # Check sorting dropdown visibility
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "select")))
            self.assertIsNotNone(sort_dropdown, "Sort dropdown is missing")

            # Check product list visibility
            products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
            self.assertIsNotNone(products, "Products section is missing")

            # Check click on the first product
            first_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".products .column a")))
            first_product.click()

            # Confirm navigation to product page
            product_details = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "product-name"))
            )
            self.assertIsNotNone(product_details, "Product details not visible after clicking the product link")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()