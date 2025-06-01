import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestKeyUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://max/search')

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for navigation links
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            
            # Wait for search input
            search_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-box-button")))

            # Check if the links and buttons are displayed
            self.assertTrue(search_input.is_displayed(), "Search input not displayed")
            self.assertTrue(search_button.is_displayed(), "Search button not displayed")
            
            # Click search button
            search_input.send_keys("book")
            search_button.click()

            # Verify elements in search results
            product_grid = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-grid")))
            self.assertTrue(product_grid.is_displayed(), "Product grid not displayed after searching")

            # Check advanced search toggle
            adv_search_toggle = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "advs")))
            self.assertTrue(adv_search_toggle.is_displayed(), "Advanced search toggle not displayed")
            adv_search_toggle.click()

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()