from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/category-a-1")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for header to be present and visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Wait for footer to be present and visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "footer"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".primary-nav a")
        if not nav_links:
            self.fail("Navigation links are missing")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), "Navigation link is not visible")

        # Check the search input field
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check that the sort select dropdown is visible
        sort_select = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".select select"))
        )
        self.assertTrue(sort_select.is_displayed(), "Sort select dropdown is not visible")

        # Check the logo is visible in the header
        logo_img = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img"))
        )
        self.assertTrue(logo_img.is_displayed(), "Logo is not visible")

        # Interacting with filter button (For mobile filter button test, if applicable on desktop)
        filter_button = driver.find_element(By.CSS_SELECTOR, ".is-hidden-tablet .button")
        self.assertTrue(filter_button.is_displayed(), "Filter button is not visible")

        # Click filter button and check if anything opens
        filter_button.click()

        # Use WebDriverWait to ensure UI changes
        # An example could be waiting for a filter modal or section to be visible
        # If there's a known expected UI change after clicking, replace the selector below
        try:
            filter_modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".attribute-filter"))
            )
            self.assertTrue(filter_modal.is_displayed(), "Filter modal is not visible after clicking filter button")
        except Exception as e:
            self.fail(f"Filter modal did not appear: {str(e)}")
            
        # Assert that important elements are not missing
        required_elements = [
            ".search-input", 
            ".select select", 
            ".logo-image img",
            ".primary-nav a",
        ]
        for selector in required_elements:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if not elements:
                self.fail(f"Required element with selector '{selector}' is missing")
            for element in elements:
                self.assertTrue(element.is_displayed(), f"Element with selector '{selector}' is not visible")

if __name__ == "__main__":
    unittest.main()