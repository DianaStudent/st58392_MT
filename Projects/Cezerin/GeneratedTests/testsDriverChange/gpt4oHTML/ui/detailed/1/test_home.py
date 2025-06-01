import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://your-website-url.com")  # Replace with actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check the visibility of the header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not present or visible on the page")

        # Check the visibility of the footer
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not present or visible on the page")

        # Check the primary navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".primary-nav .cat-parent a")
        self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are present or visible")

        # Check input field and button visibility in search box
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box .search-input")))
        self.assertIsNotNone(search_input, "Search input field is not visible")

        search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-icon-search")))
        self.assertIsNotNone(search_button, "Search button is not visible")

        # Check the banner slider presence
        slider = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "home-slider")))
        self.assertIsNotNone(slider, "Home slider is not present or visible")

        # Check the 'BEST SELLERS' section title
        best_sellers_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4.has-text-centered")))
        self.assertEqual(best_sellers_title.text, 'BEST SELLERS', "BEST SELLERS title is missing or incorrect")

        # Interact with the first category link
        first_category = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".primary-nav a[href='/category-a']")))
        first_category.click()

        # Confirm navigation to Category A
        category_header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".container .title")))
        self.assertIn('Category A', category_header.text, "Did not navigate to Category A page")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()