from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):
    @classmethod
    def setUp(cls):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("http://localhost:3000")
        cls.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible or does not exist.")

        # Check navigation links
        try:
            nav_links = driver.find_elements(By.CSS_SELECTOR, ".primary-nav .cat-parent a")
            self.assertTrue(all(link.is_displayed() for link in nav_links), "Not all navigation links are visible.")
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img")))
        except:
            self.fail("Logo is not visible or does not exist.")
        
        # Check search box
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        except:
            self.fail("Search input is not visible or does not exist.")
        
        # Check banner image
        try:
            banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".image-gallery-image img")))
        except:
            self.fail("Banner image is not visible or does not exist.")
        
        # Check "BEST SELLERS" section
        try:
            best_sellers = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
            self.assertEqual(best_sellers.text, "BEST SELLERS", "BEST SELLERS section title is incorrect.")
        except:
            self.fail("BEST SELLERS section is not visible or does not exist.")

        # Check for products
        try:
            products = driver.find_elements(By.CSS_SELECTOR, ".products .product-caption")
            self.assertTrue(all(product.is_displayed() for product in products), "Not all products are visible.")
        except:
            self.fail("Products are missing or not visible.")

        # Interact with search
        search_keyword = "Product A"
        search_input.clear()
        search_input.send_keys(search_keyword)
        
        try:
            search_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-icon-search")))
            search_icon.click()
        except:
            self.fail("Search icon is not clickable or does not exist.")
        
        # Verify that no errors are shown
        try:
            error_banner = driver.find_elements(By.CLASS_NAME, "error")
            self.assertEqual(len(error_banner), 0, "Error banner should not be present.")
        except:
            self.fail("Error banner check failed.")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()