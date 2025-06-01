import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check for header
        header = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'header'))
        )
        self.assertIsNotNone(header, "Header is missing or not visible.")

        # Check for footer
        footer = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
        )
        self.assertIsNotNone(footer, "Footer is missing or not visible.")

        # Check for navigation menu
        nav_menu = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav'))
        )
        self.assertIsNotNone(nav_menu, "Navigation menu is missing or not visible.")

        # Check for search input
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'search-input'))
        )
        self.assertIsNotNone(search_input, "Search input is missing or not visible.")

        # Check for cart icon
        cart_icon = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button'))
        )
        self.assertIsNotNone(cart_icon, "Cart icon is missing or not visible.")

        # Check for product section
        product_section = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'products'))
        )
        self.assertIsNotNone(product_section, "Product section is missing or not visible.")

        # Check for 'BEST SELLERS' label
        best_sellers_label = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'title'))
        )
        self.assertIsNotNone(best_sellers_label, "'BEST SELLERS' label is missing or not visible.")

        # Click on a category link and verify
        category_a_link = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'Category A'))
        )
        category_a_link.click()

        # Verify URL for category page
        self.wait.until(EC.url_to_be("http://localhost:3000/category-a"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()