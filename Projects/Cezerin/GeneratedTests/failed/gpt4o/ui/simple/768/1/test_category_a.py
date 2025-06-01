from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check for logo
        logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        self.assertTrue(logo.is_displayed(), "Logo is not visible")

        # Check for search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check for navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav .cat-parent a')
        self.assertTrue(all(link.is_displayed() for link in nav_links), "Not all navigation links are visible")

        # Check for filter section
        filter_section = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'left-sidebar')))
        self.assertTrue(filter_section.is_displayed(), "Filter section is not visible")

        # Check for sort select
        sort_select = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort select')))
        self.assertTrue(sort_select.is_displayed(), "Sort select is not visible")

        # Check for products
        products = driver.find_elements(By.CSS_SELECTOR, '.products .column')
        self.assertTrue(all(product.is_displayed() for product in products), "Not all products are visible")

        # Check for footer
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()