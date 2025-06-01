import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header visibility
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertIsNotNone(header)

            # Check footer visibility
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertIsNotNone(footer)

            # Check navigation visibility
            nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
            self.assertIsNotNone(nav)

            # Check search input field visibility
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            self.assertIsNotNone(search_input)

            # Check for presence of product section
            product_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.products')))
            self.assertIsNotNone(product_section)

            # Interact with sort dropdown
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort select')))
            sort_dropdown.click()
            sort_option = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'option[value="-date_created"]')))
            sort_option.click()

            # Check for presence of 'Sort' label
            sort_label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort-title')))
            self.assertIsNotNone(sort_label)

            # Check if products are visible
            products = driver.find_elements(By.CSS_SELECTOR, '.products .product-caption')
            self.assertGreater(len(products), 0, "No products found on the page.")

        except Exception as e:
            self.fail(f"Test failed due to missing elements or interaction failure: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()