import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    def setUp(self):
        # Setup Chrome webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def test_ui_elements(self):
        driver = self.driver
        driver.get(self.base_url)

        # Define elements to check
        elements_to_check = [
            (By.CLASS_NAME, 'header'),  # Header
            (By.CLASS_NAME, 'header-links'),  # Navigation links in header
            (By.ID, 'small-search-box-form'),  # Search form
            (By.ID, 'small-searchterms'),  # Search input box
            (By.CLASS_NAME, 'button-1'),  # Any button element
            (By.CLASS_NAME, 'footer-upper'),  # Footer
        ]

        for locator in elements_to_check:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(locator)
                )
                self.assertTrue(element.is_displayed(), f"Element {locator} is not visible")
            except Exception as e:
                self.fail(f"Failed to find element with locator: {locator}. Exception: {e}")

        # Interact with a button and verify UI updates
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'small-searchterms'))
            )
            search_input.send_keys("Test Product")

            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'search-box-button'))
            )
            search_button.click()

            # Verify that the search yields results or UI updates
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ui-autocomplete'))
            )
        except Exception as e:
            self.fail(f"Interactive element test failed. Exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()