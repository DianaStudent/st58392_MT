from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Verify header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img")))
        except:
            self.fail("Logo is not visible")

        # Verify navigation links
        try:
            nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".nav-level-0 li a")))
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are visible")
        except:
            self.fail("Navigation links are not visible")

        # Verify search box
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        except:
            self.fail("Search input is not visible")

        # Verify cart icon
        try:
            cart_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img")))
        except:
            self.fail("Cart icon is not visible")

        # Verify Filter products button
        try:
            filter_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.is-fullwidth")))
            self.assertIn("Filter products", filter_button.text)
        except:
            self.fail("Filter products button is not visible")

        # Click the sort dropdown and verify options
        try:
            sort_select = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort select")))
            sort_select.click()
            sort_options = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".sort select option")))
            self.assertGreaterEqual(len(sort_options), 4, "Not all sort options are visible")
        except:
            self.fail("Sort select or options are not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()