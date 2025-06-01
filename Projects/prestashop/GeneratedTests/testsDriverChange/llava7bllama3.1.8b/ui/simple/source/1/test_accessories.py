from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_homepage_elements(self):
        # Check that main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        
        # Check header and navigation elements exist and are visible
        self.assertTrue(WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        ))
        self.assertTrue(WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//nav"))
        ))

    def test_clothes_page_elements(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        
        # Check that product category and product list elements exist
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='category-name']"))
        )
        self.assertTrue(WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='product-list']"))
        ))

    def test_accessories_page_elements(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        
        # Check that product category and product list elements exist
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='category-name']"))
        )
        self.assertTrue(WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='product-list']"))
        ))

    def test_art_page_elements(self):
        self.driver.get("http://localhost:8080/en/9-art")
        
        # Check that product category and product list elements exist
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='category-name']"))
        )
        self.assertTrue(WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='product-list']"))
        ))

    def test_login_page_elements(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        
        # Check that form and buttons exist
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//form"))
        )
        self.assertTrue(WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        ))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()