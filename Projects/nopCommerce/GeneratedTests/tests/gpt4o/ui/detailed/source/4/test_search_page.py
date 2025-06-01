from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver
        wait = self.wait

        # Verify header is present
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header:
            self.fail("Header is missing!")

        # Verify footer is present
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer:
            self.fail("Footer is missing!")

        # Verify navigation menu is present
        navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
        if not navigation:
            self.fail("Navigation menu is missing!")

        # Verify search box is present
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        if not search_box:
            self.fail("Search box is missing!")

        # Verify search button is present
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        if not search_button:
            self.fail("Search button is missing!")

        # Verify search label is present
        search_label = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@for='q']")))
        if not search_label:
            self.fail("Search label is missing!")

        # Verify advanced search checkbox is present
        advanced_search_checkbox = wait.until(EC.visibility_of_element_located((By.ID, "advs")))
        if not advanced_search_checkbox:
            self.fail("Advanced search checkbox is missing!")

        # Verify product grid is present
        product_grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        if not product_grid:
            self.fail("Product grid is missing!")

        # Interact with search input
        search_box.send_keys("test")

        # Interact with search button
        search_button.click()

        # Verify results or UI changes, e.g., URL change
        wait.until(EC.url_contains("search?q=test"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()