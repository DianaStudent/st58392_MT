from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestSearchPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check presence and visibility of header elements
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        self.assertIsNotNone(header, "Header is missing or not visible.")

        # Check presence and visibility of input fields and buttons
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertIsNotNone(search_box, "Search box is missing or not visible.")

        search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
        self.assertIsNotNone(search_button, "Search button is missing or not visible.")

        # Interact with key UI elements and check reactions
        search_box.send_keys("book")
        search_button.click()

        # Check presence and visibility of footer elements
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))
        self.assertIsNotNone(footer, "Footer is missing or not visible.")

        # Check presence and visibility of product grid
        product_grid = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-grid")))
        self.assertIsNotNone(product_grid, "Product grid is missing or not visible.")

        # Check presence and visibility of navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu.notmobile a")
        if not nav_links:
            self.fail("Navigation links are missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()