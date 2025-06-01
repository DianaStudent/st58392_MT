import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class NopCommerceUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/search")

    def test_main_ui_elements(self):
        driver = self.driver
        
        # Wait for and verify header elements
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )
        except:
            self.fail("Header is not visible")
        
        # Wait for and verify footer elements
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
            )
        except:
            self.fail("Footer is not visible")
        
        # Check search input field
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search input field is missing or not visible")
        
        # Check search button
        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
        except:
            self.fail("Search button is missing or not visible")
        
        # Interact with the search field and button
        search_input.send_keys("book")
        search_button.click()
        
        # Verify interaction by checking a result element
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "products-container"))
            )
        except:
            self.fail("Products container is missing or not visible after search")
        
        # Check price filter
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "price-range-filter"))
            )
        except:
            self.fail("Price range filter is missing or not visible")
        
        # Check and interact with "View as" grid/list buttons
        try:
            view_as_grid = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".viewmode-icon.grid"))
            )
            view_as_list = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".viewmode-icon.list"))
            )
            view_as_grid.click()
            view_as_list.click()
        except:
            self.fail("View as grid or list buttons are missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)