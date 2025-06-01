import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8," + html_data["html"])
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except Exception:
            self.fail("Header not found or not visible")

        # Check Navigation Links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav .nav-level-0 > li > .cat-parent > a")))
            self.assertGreaterEqual(len(nav_links), 1, "Navigation links are missing")
        except Exception:
            self.fail("Navigation links not found or not visible")

        # Check Search input
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box .search-input")))
        except Exception:
            self.fail("Search input not found or not visible")

        # Check Cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img")))
        except Exception:
            self.fail("Cart button not found or not visible")

        # Check Product Filters
        try:
            filter_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.is-fullwidth.is-dark.is-hidden-tablet")))
        except Exception:
            self.fail("Filter button not found or not visible")

        # Check Sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".select.is-fullwidth select")))
        except Exception:
            self.fail("Sort dropdown not found or not visible")

        # Check Product Listings
        try:
            products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products .available")))
            self.assertGreaterEqual(len(products), 1, "Product listings are missing")
        except Exception:
            self.fail("Product listings not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    html_data = {
        "html": "<html lang=\"en\">......</html>"  # Placeholder for the provided html content
    }
    unittest.main()