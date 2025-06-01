from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AccessoriesPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        
    def tearDown(self):
        self.driver.quit()

    def test_UI_elements_present_and_visible(self):
        driver = self.driver
        
        try:
            # Check if the main header is visible
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
            
            # Check if the main menu category links are visible
            clothes_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"))
            )
            accessories_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"))
            )
            art_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            
            # Check if the login and register links are visible
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']"))
            )
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']"))
            )
            
            # Check if the search bar is visible
            search_bar = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "s"))
            )
            
            # Check if the category breadcrumb is visible
            breadcrumb = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb"))
            )
            
            # Check if the product list is visible
            product_list = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "js-product-list"))
            )
            
        except Exception as e:
            self.fail(f"An expected UI element is missing: {str(e)}")

if __name__ == "__main__":
    unittest.main()