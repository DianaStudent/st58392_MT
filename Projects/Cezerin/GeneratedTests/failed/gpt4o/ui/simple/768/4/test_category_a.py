from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not present or not visible.")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        except:
            self.fail("Search input field is not present or not visible.")

        # Check category link
        try:
            category_link = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//a[@href='/category-a' and contains(text(), 'Category A')]")
            ))
        except:
            self.fail("Category A link is not present or not visible.")

        # Check product links
        product_links = [
            '/category-a/product-a',
            '/category-a/product-b'
        ]
        for product_link in product_links:
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{product_link}']")))
            except:
                self.fail(f"Product link {product_link} is not present or not visible.")

        # Check subcategory links
        subcategory_links = [
            '/category-a-1',
            '/category-a-2',
            '/category-a-3'
        ]
        for subcat_link in subcategory_links:
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{subcat_link}']")))
            except:
                self.fail(f"Subcategory link {subcat_link} is not present or not visible.")

        # Check the shopping cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.cart-button')))
        except:
            self.fail("Cart button is not present or not visible.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is not present or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()