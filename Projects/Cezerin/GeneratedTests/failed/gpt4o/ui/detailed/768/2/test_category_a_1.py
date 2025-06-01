from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Verify header is visible
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header:
            self.fail("Header is not visible")

        # Verify footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        if not footer:
            self.fail("Footer is not visible")

        # Verify main logo link
        logo_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo-image')))
        if not logo_link:
            self.fail("Main logo link is not visible")

        # Verify search input
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        if not search_input:
            self.fail("Search input is not visible")
        
        # Verify cart button
        cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button')))
        if not cart_button:
            self.fail("Cart button is not visible")

        # Verify category navigation
        category_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
        if not category_nav:
            self.fail("Category navigation is not visible")

        # Verify breadcrumb
        breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
        if not breadcrumb:
            self.fail("Breadcrumb is not visible")

        # Verify sort select dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//select")))
        if not sort_dropdown:
            self.fail("Sort dropdown is not visible")

        # Verify Subcategory 1 title
        subcategory_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        if not subcategory_title:
            self.fail("Subcategory 1 title is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()