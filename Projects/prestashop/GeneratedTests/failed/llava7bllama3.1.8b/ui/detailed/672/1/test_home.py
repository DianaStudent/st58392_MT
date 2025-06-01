from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestWebsite(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_page_structure(self):
        # Check header presence and visibility
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        
        # Check footer presence and visibility
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check search bar existence and visibility
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#searchbar-autocomplete")
        except NoSuchElementException:
            self.fail("Search bar is missing")

    def test_main_content(self):
        # Check presence of main content elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-autocomplete")))

        # Check product cards existence and visibility
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".product-card")
        except NoSuchElementException:
            self.fail("Product cards are missing")

    def test_features_products(self):
        # Check featured products section presence and visibility
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#featured-products")))

        # Check product images existence and visibility
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".product-image")
        except NoSuchElementException:
            self.fail("Product images are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()