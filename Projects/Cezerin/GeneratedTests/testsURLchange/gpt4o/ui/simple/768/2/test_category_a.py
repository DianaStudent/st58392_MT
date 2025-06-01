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

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertIsNotNone(header)

            # Category Navigation
            category_nav = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            self.assertIsNotNone(category_nav)

            subcategory_1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']")))
            self.assertIsNotNone(subcategory_1)

            # Search Box
            search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
            self.assertIsNotNone(search_box)

            # Add to Cart (although button is implicit in this context)
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon')))
            self.assertIsNotNone(cart_icon)

            # Footer
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertIsNotNone(footer)

            # Product List
            product_a = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
            self.assertIsNotNone(product_a)

            product_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-b']")))
            self.assertIsNotNone(product_b)

            # Sort Dropdown
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'select')))
            self.assertIsNotNone(sort_dropdown)

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()