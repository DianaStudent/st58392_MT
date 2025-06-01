import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Log in')))
            
            # Check search box
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            self.assertIsNotNone(search_box)
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
            self.assertIsNotNone(search_button)
            
            # Check main menu
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home page')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'New products')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Search')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My account')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Blog')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))

            # Check advanced search elements
            advanced_search_checkbox = wait.until(EC.visibility_of_element_located((By.ID, 'advs')))
            self.assertIsNotNone(advanced_search_checkbox)

            # Check product items
            product_items = driver.find_elements(By.CLASS_NAME, 'product-item')
            if not product_items:
                self.fail("Product items are not visible or missing.")

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()