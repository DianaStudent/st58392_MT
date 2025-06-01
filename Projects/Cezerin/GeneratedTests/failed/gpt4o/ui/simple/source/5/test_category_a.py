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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header:
            self.fail("Header not found or not visible")

        # Check category title
        category_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.category-title')))
        if category_title.text != "Category A":
            self.fail("Category title is not 'Category A'")

        # Check that filter elements are present and visible
        brand_filter = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.attribute-title')))
        if brand_filter.text != "Brand":
            self.fail("Brand filter not found or not visible")

        # Check product elements
        products = driver.find_elements(By.CSS_SELECTOR, '.content.product-caption')
        if len(products) == 0:
            self.fail("No products found or products are not visible")
        for product in products:
            product_name = product.find_element(By.CLASS_NAME, 'product-name')
            product_price = product.find_element(By.CLASS_NAME, 'product-price')
            if not product_name.is_displayed() or not product_price.is_displayed():
                self.fail("Product name or price not visible")

        # Check footer elements
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        if not footer:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()