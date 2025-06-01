import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check header exists and is visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header')))
        header = self.driver.find_element(By.CSS_SELECTOR, 'header')
        self.assertTrue(header.is_displayed())

        # Check logo or brand name exists and is visible
        logo = self.driver.find_element(By.CSS_SELECTOR, '.logo')
        self.assertTrue(logo.is_displayed())

        # Check navigation menu exists and is visible
        nav_menu = self.driver.find_element(By.CSS_SELECTOR, 'nav ul')
        self.assertTrue(nav_menu.is_displayed())

        # Check search bar exists and is visible
        search_bar = self.driver.find_element(By.CSS_SELECTOR, '.search-bar')
        self.assertTrue(search_bar.is_displayed())

        # Check main content area exists and is visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#main-content')))
        main_content = self.driver.find_element(By.CSS_SELECTOR, '#main-content')
        self.assertTrue(main_content.is_displayed())

        # Check footer exists and is visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer')))
        footer = self.driver.find_element(By.CSS_SELECTOR, 'footer')
        self.assertTrue(footer.is_displayed())

if __name__ == "__main__":
    unittest.main()