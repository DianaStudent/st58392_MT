import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Verify navigation links are visible
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu .category")
        self.assertGreater(len(nav_links), 0, "Navigation links are missing")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), "A navigation link is not visible")

        # Verify login button is visible
        login_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")

        # Verify search input field is visible
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[type='text']")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")

        # Verify product list is present
        products = driver.find_elements(By.CSS_SELECTOR, ".products .product-miniature")
        self.assertGreater(len(products), 0, "Product list is missing")

        # Check product title and price
        for product in products:
            title = product.find_element(By.CSS_SELECTOR, ".product-title")
            price = product.find_element(By.CSS_SELECTOR, ".price")
            self.assertTrue(title.is_displayed(), f"Product title is not visible for {title.text}")
            self.assertTrue(price.is_displayed(), f"Product price is not visible for {title.text}")

        # Test interaction with the search input
        search_input.click()
        search_input.send_keys("poster")
        
        # Verify Filter button is visible and functional
        filter_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_filter_toggler")))
        self.assertTrue(filter_button.is_displayed(), "Filter button is not visible")
        filter_button.click()
        
        # Verify the UI reacts
        active_search_filters = self.wait.until(EC.visibility_of_element_located((By.ID, "js-active-search-filters")))
        self.assertTrue(active_search_filters.is_displayed(), "Search filters did not appear")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()