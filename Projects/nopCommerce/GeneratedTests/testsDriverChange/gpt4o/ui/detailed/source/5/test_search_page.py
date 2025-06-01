import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestNopCommercePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header"))
            )
        except:
            self.fail("Header is not visible")

        # Check footer
        try:
            footer = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer"))
            )
        except:
            self.fail("Footer is not visible")

        # Check search input field
        try:
            search_input = self.wait.until(
                EC.visibility_of_element_located((By.ID, "q"))
            )
        except:
            self.fail("Search input field is not visible")

        # Check search button
        try:
            search_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-button"))
            )
        except:
            self.fail("Search button is not visible")

        # Check advanced search toggle and its functionality
        try:
            adv_search_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.ID, "advs"))
            )
        except:
            self.fail("Advanced search checkbox is not visible")

        # Interact with UI: Click advanced search and verify visibility
        adv_search_checkbox.click()

        try:
            adv_search_block = self.wait.until(
                EC.visibility_of_element_located((By.ID, "advanced-search-block"))
            )
        except:
            self.fail("Advanced search block is not visible after clicking")

        # Check if product grid is visible
        try:
            product_grid = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-grid"))
            )
        except:
            self.fail("Product grid is not visible")

        # Check "Add to cart" button for first product and click
        try:
            add_to_cart_button = self.wait.until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR,
                    ".product-box-add-to-cart-button"
                ))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button is not visible or clickable")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()