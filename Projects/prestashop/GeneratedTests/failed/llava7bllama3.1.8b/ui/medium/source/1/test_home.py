from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        # Check navigation links
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-item")))
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, ".nav-item")
        for link in nav_links:
            self.assertTrue(link.is_displayed())

        # Check inputs and buttons
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "search-bar-input")))
        search_input = self.driver.find_element(By.ID, "search-bar-input")
        self.assertTrue(search_input.is_displayed())
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, ".search-btn")
        self.assertTrue(search_button.is_displayed())

    def test_interaction(self):
        # Click the 'Shop now' button
        shop_now_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shop now")))
        shop_now_button.click()

        # Check that the UI updates visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shop-now-results")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()