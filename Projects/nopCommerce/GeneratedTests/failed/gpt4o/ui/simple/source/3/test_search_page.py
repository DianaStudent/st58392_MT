from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/search')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        header_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))
        self.assertIsNotNone(header_menu, "Header menu is not visible")

        # Check search form elements
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        self.assertIsNotNone(search_box, "Search box form is not visible")

        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertIsNotNone(search_input, "Search input is not visible")

        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-box-button")))
        self.assertIsNotNone(search_button, "Search button is not visible")

        # Check main page elements
        main_content = wait.until(EC.visibility_of_element_located((By.ID, "main")))
        self.assertIsNotNone(main_content, "Main content is not visible")

        # Check product grid elements
        product_grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        self.assertIsNotNone(product_grid, "Product grid is not visible")

        # Verify each product item in the grid
        products = driver.find_elements(By.CLASS_NAME, "product-item")
        self.assertGreater(len(products), 0, "No products found in product grid")

        # Check for footer elements
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible")

if __name__ == "__main__":
    unittest.main()