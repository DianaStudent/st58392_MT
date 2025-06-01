import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_visibility(self):
        self.driver.get("http://localhost:3000/category-a-1")
        
        # Check for header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not visible.")

        # Check for main logo
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image img[alt="logo"]')))
        self.assertIsNotNone(logo, "Logo is not visible.")

        # Check for navigation links
        nav_links = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
        self.assertIsNotNone(nav_links, "Navigation links are not visible.")

        # Check for search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-box .search-input')))
        self.assertIsNotNone(search_input, "Search input is not visible.")

        # Check for cart button
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button img[alt="cart"]')))
        self.assertIsNotNone(cart_button, "Cart button is not visible.")

        # Check for breadcrumb
        breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
        self.assertIsNotNone(breadcrumb, "Breadcrumb is not visible.")

        # Check for category title
        category_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.category-title')))
        self.assertIsNotNone(category_title, "Category title is not visible.")

        # Check for footer
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not visible.")

        # Check for presence of a footer logo
        footer_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer-logo img')))
        self.assertIsNotNone(footer_logo, "Footer logo is not visible.")

        # Interact with category link
        category_a_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Category A')))
        category_a_link.click()
        
        # Assert that clicking the link loads the correct page
        self.wait.until(EC.url_contains("/category-a"), "Didn't navigate to Category A.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()