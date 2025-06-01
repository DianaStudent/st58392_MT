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
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not present or visible")

        # Check for navigation links
        try:
            nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul.nav-level-0 > li > div > a')))
        except:
            self.fail("Navigation links are not present or visible")
        
        # Check for search input presence
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search input is not present or visible")

        # Check for home slider
        try:
            home_slider = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'home-slider')))
        except:
            self.fail("Home slider is not present or visible")

        # Check for best sellers section
        try:
            best_sellers = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))
            self.assertEqual(best_sellers.text, "BEST SELLERS")
        except:
            self.fail("Best Sellers section is not present or visible")

        # Interact with search input and check no errors
        search_input.send_keys("test")
        # Integration with other UI checks can be added here, for example clicking search or checking results.

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()