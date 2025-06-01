from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver
        wait = self.wait

        # Check top navigation links
        top_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "top-menu")))
        self.assertTrue(top_menu.is_displayed(), "Top menu is not displayed")

        # Check search input
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        self.assertTrue(search_input.is_displayed(), "Search input is not displayed")

        # Check search button
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        self.assertTrue(search_button.is_displayed(), "Search button is not displayed")

        # Check product grid
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        self.assertTrue(product_grid.is_displayed(), "Product grid is not displayed")

        # Interact with a button
        view_grid_mode = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".viewmode-icon.grid")))
        view_grid_mode.click()
        
        # Check a UI update visually, e.g., grid view is selected
        grid_selected = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".viewmode-icon.grid.selected")))
        self.assertTrue(grid_selected.is_displayed(), "Grid mode is not selected after clicking")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()