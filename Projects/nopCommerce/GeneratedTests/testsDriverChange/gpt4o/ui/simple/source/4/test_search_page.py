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
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver

        # Check header elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links")))

        # Check links
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

        # Check the search form
        self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))

        # Check navigation menu
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))

        # Check search page elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "buttons")))

        # Check filters
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-filters")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "price-range-filter")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-title")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-content")))

        # Check products
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-container")))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()