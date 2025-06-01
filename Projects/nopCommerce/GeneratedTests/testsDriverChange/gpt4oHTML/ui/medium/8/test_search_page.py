import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check for header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except:
            self.fail("Header element is missing or not visible.")

        # Check for search box
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            self.assertTrue(search_box.is_displayed(), "Search box is not visible")
        except:
            self.fail("Search box is missing or not visible.")

        # Check for the search button
        try:
            search_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-box-button')))
            self.assertTrue(search_button.is_displayed(), "Search button is not clickable or visible")
        except:
            self.fail("Search button is missing or not visible.")

        # Check interactive element - Advanced search
        try:
            advanced_search_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, 'advs')))
            self.assertTrue(advanced_search_checkbox.is_displayed(), "Advanced search checkbox is not visible")
            advanced_search_checkbox.click()
            # Verify UI updates - Advanced search section should be visible
            advanced_search_section = self.wait.until(EC.visibility_of_element_located((By.ID, 'advanced-search-block')))
            self.assertTrue(advanced_search_section.is_displayed(), "Advanced search block did not appear after clicking the checkbox.")
        except:
            self.fail("Advanced search checkbox interaction failed or is missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()