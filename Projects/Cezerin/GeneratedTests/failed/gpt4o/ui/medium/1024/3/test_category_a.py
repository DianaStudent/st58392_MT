from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements_present(self):
        driver = self.driver

        try:
            # Wait for header and verify visibility
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
            )

            # Verify navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, ".primary-nav .cat-parent a")
            self.assertTrue(all(link.is_displayed() for link in nav_links), "Not all navigation links are visible.")

            # Verify search input
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box .search-input"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

            # Verify search button
            search_button = driver.find_element(By.CSS_SELECTOR, ".search-box .search-icon-search")
            self.assertTrue(search_button.is_displayed(), "Search button is not visible.")

            # Verify category breadcrumbs
            breadcrumb = driver.find_element(By.CSS_SELECTOR, "nav.breadcrumb")
            self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb is not visible.")

            # Verify product listing
            products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
            self.assertTrue(all(product.is_displayed() for product in products), "Not all products are visible.")

            # Verify filter button (mobile version)
            filter_button = driver.find_element(By.CSS_SELECTOR, "button.is-fullwidth")
            self.assertTrue(filter_button.is_displayed(), "Filter button is not visible.")

            # Interaction test: click search icon and ensure input is focused
            search_button.click()
            self.assertEqual(driver.switch_to.active_element, search_input, "Search input is not focused after clicking search button.")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()