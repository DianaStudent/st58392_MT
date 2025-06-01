import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_main_page_elements_present_and_visible(self):
        # Navigate to the page
        self.driver.get("https://your-page.com")

        # Wait for main UI components to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#home")))  
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".category_a")))   
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".category_a_1")))  

        # Check that required elements are present and visible
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "#home").is_enabled())
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".category_a").is_enabled()) 
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".category_a_1").is_enabled())

if __name__ == '__main__':
    unittest.main()