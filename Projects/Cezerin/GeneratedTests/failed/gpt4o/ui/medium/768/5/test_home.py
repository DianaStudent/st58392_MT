from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for elements to load and check visibility
        wait = WebDriverWait(driver, 20)

        try:
            # Verify header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))

            # Verify search input
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
            
            # Verify banner
            banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image-gallery")))
            self.assertTrue(banner.is_displayed(), "Banner is not visible")
            
            # Verify product listings
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-name")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-price")))

            # Interact with an element
            category_a_link = driver.find_element(By.LINK_TEXT, "Category A")
            category_a_link.click()

            # Verify page navigation
            wait.until(EC.url_to_be("http://localhost:3000/category-a"))

        except Exception as e:
            self.fail(f"Test failed due to missing or invisible element: {e}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()