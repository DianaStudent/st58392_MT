from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header:
            self.fail("Header is missing.")

        # Verify navigation links are visible
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav a')))
        if len(nav_links) == 0:
            self.fail("Navigation links are missing.")

        # Verify search input visibility
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        if not search_input:
            self.fail("Search input field is missing.")
        
        # Verify carousel elements
        carousel_images = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.image-gallery-image img')))
        if len(carousel_images) == 0:
            self.fail("Carousel images are missing.")
        
        # Verify 'BEST SELLERS' section
        best_sellers_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title.is-4')))
        if not best_sellers_title:
            self.fail("Best sellers title is missing.")
        
        # Verify footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        if not footer:
            self.fail("Footer is missing.")
        
        # Interact with the search button
        search_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.icon.icon-search')))
        search_icon.click()

        # Interact with navigation to Category A
        category_a_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
        category_a_link.click()

        # Confirm navigation to Category A
        self.wait.until(EC.url_contains("category-a"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()