import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Header Links
        header_links = [
            (By.LINK_TEXT, "Register"),
            (By.LINK_TEXT, "Log in"),
            (By.LINK_TEXT, "Wishlist"),
            (By.LINK_TEXT, "Shopping cart")
        ]
        for by, link in header_links:
            try:
                wait.until(EC.visibility_of_element_located((by, link)))
            except:
                self.fail(f"The link with text '{link}' is not visible.")

        # Header Menu
        menu_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]
        for by, link in menu_links:
            try:
                wait.until(EC.visibility_of_element_located((by, link)))
            except:
                self.fail(f"The menu link with text '{link}' is not visible.")

        # Search Box
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button-1.search-box-button")))
        except:
            self.fail("Search box or its components are not visible.")

        # Search Results
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-results")))
        except:
            self.fail("Search input or search results are not visible.")

        # Product Filters
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-filter")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "price-range-filter")))
        except:
            self.fail("Product filters are not visible.")
        
        # Product Grid
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-container")))
        except:
            self.fail("Products container is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()