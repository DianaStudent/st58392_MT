from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
    
    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        except:
            self.fail("Header is not visible")

        # Verify navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav .cat-parent a")))
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are present")
        except:
            self.fail("Navigation links are not visible")

        # Verify search box
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        except:
            self.fail("Search input is not visible")

        # Verify cart button
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        except:
            self.fail("Cart button is not visible")

        # Verify sort dropdown
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort select")))
        except:
            self.fail("Sort dropdown is not visible")

        # Interact with sort dropdown
        try:
            sort_dropdown = driver.find_element(By.CSS_SELECTOR, ".sort select")
            sort_dropdown.click()
            option = driver.find_element(By.CSS_SELECTOR, ".sort select option[value='price']")
            option.click()

            # Verify UI updates visually, e.g., no errors or exceptions
            product_sections = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".section-category")))
            self.assertIsNotNone(product_sections, "Product section is not updating correctly")
        except:
            self.fail("Interacting with sort dropdown failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()