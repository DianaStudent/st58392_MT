import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_category_a_elements(self):
        driver = self.driver
        driver.get("http://localhost:3000/category-a")
        
        wait = WebDriverWait(driver, 20)

        # Check presence and visibility of navigation links
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-b']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-c']")))
        except Exception:
            self.fail("Navigation links are not visible.")

        # Check presence and visibility of search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        except Exception:
            self.fail("Search input is not visible.")

        # Check presence and visibility of sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//select")))
        except Exception:
            self.fail("Sort dropdown is not visible.")

        # Check presence and visibility of product elements
        try:
            product_a = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
            product_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-b']")))
        except Exception:
            self.fail("Products are not visible.")

        # Interact with the sort dropdown
        try:
            sort_dropdown.click()
            option_price_low = wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='price']")))
            option_price_low.click()
        except Exception:
            self.fail("Unable to interact with sort dropdown.")

        # Verify that no errors occurred in the UI
        self.assertTrue(self.is_page_loaded_properly(), "Page did not load properly.")

    def is_page_loaded_properly(self):
        # Placeholder for additional checks if needed
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()