import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of the header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header:
            self.fail("Header not visible")

        # Check visibility of the footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer:
            self.fail("Footer not visible")

        # Check navigation elements
        navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
        if not navigation:
            self.fail("Navigation menu not visible")

        # Check presence and visibility of input fields, buttons, etc.
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        if not search_input:
            self.fail("Search input not visible")

        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        if not search_button:
            self.fail("Search button not visible")

        # Interact with the UI elements
        search_input.send_keys("book")
        search_button.click()

        # Confirm the UI reacts visually
        search_results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-results")))
        if not search_results:
            self.fail("Search results not visible after clicking search")

        # Assert that no required UI element is missing
        try:
            product_items = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-item")))
            if not product_items:
                self.fail("No product items found in search results")
        except:
            self.fail("No product items found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()