import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_main_page_elements(self):
        self.driver.get("http://localhost:8080/en/")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        
        header = self.driver.find_element(By.XPATH, "//h1[@class='page-title']")
        self.assertIsNotNone(header)
        
        # Check that the navigation menu is present
        nav_menu = self.driver.find_elements(By.XPATH, "//ul[@id='nav-menu']/li")
        self.assertGreaterEqual(len(nav_menu), 5)

    def test_clothes_page_elements(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        
        header = self.driver.find_element(By.XPATH, "//h1[@class='page-title']")
        self.assertIsNotNone(header)
        
    def test_accessories_page_elements(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        
        header = self.driver.find_element(By.XPATH, "//h1[@class='page-title']")
        self.assertIsNotNone(header)
        
    def test_art_page_elements(self):
        self.driver.get("http://localhost:8080/en/9-art")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        
        header = self.driver.find_element(By.XPATH, "//h1[@class='page-title']")
        self.assertIsNotNone(header)
        
    def test_login_page_elements(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        
        header = self.driver.find_element(By.XPATH, "//h1[@class='page-title']")
        self.assertIsNotNone(header)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()