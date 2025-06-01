from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header)
        except Exception:
            self.fail("Header is not visible.")

        # Check footer visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertIsNotNone(footer)
        except Exception:
            self.fail("Footer is not visible.")

        # Check navigation visibility
        try:
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "primary-nav")))
            self.assertIsNotNone(nav)
        except Exception:
            self.fail("Primary navigation is not visible.")

        # Check search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
            self.assertIsNotNone(search_input)
        except Exception:
            self.fail("Search input field is not visible.")

        # Check search icon
        try:
            search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-search")))
            self.assertIsNotNone(search_icon)
        except Exception:
            self.fail("Search icon is not visible.")

        # Interact with buttons
        try:
            sort_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sort select")))
            sort_button.click()
        except Exception:
            self.fail("Sort button is not clickable or not visible.")

        try:
            filter_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".button.is-fullwidth.is-dark.is-hidden-tablet")))
            filter_button.click()
        except Exception:
            self.fail("Filter button is not clickable or not visible.")

        # Check category title visibility
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
            self.assertIsNotNone(category_title)
        except Exception:
            self.fail("Category title is not visible.")

        # Check that necessary UI elements are visible
        necessary_elements = [
            (By.CSS_SELECTOR, ".nav-level-0"),
            (By.CSS_SELECTOR, ".product-filter"),
            (By.CSS_SELECTOR, ".price-filter-range"),
            (By.CSS_SELECTOR, ".footer-logo"),
        ]

        for locator in necessary_elements:
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
                self.assertIsNotNone(element)
            except Exception:
                self.fail(f"Element with locator {locator} is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()