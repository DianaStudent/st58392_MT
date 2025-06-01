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

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not visible")

        # Verify logo
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo-image img')))
        self.assertIsNotNone(logo, "Logo is not visible")

        # Verify search box
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        self.assertIsNotNone(search_box, "Search box is not visible")

        # Verify category nav item
        category_a = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Category A']")))
        self.assertIsNotNone(category_a, "Category A link is not visible")

        # Verify product list
        product_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.products .column')))
        self.assertTrue(len(product_list) > 0, "Product list is empty")

        # Verify product name and price
        product_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-name')))
        self.assertIsNotNone(product_name, "Product name is not visible")

        product_price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-price')))
        self.assertIsNotNone(product_price, "Product price is not visible")

        # Verify footer elements
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not visible")

        company_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.footer-menu a')))
        self.assertTrue(len(company_links) > 0, "Company links are not visible in footer")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()