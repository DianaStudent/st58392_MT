from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestHomePage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        
    def tearDown(self):
        self.driver.quit()
    
    def test_main_ui_components_present(self):
        # Headers
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#header"))
        )
        
        # Buttons
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-default']"))
        )
        
        # Links
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
        )
        
        # Form fields
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        
    def test_clothes_link_present(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
        )
        
    def test_accessories_link_present(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
        )
        
    def test_art_link_present(self):
        self.driver.get("http://localhost:8080/en/9-art")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
        )
        
    def test_login_link_present(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        )
        
    def test_register_link_present(self):
        self.driver.get("http://localhost:8080/en/registration")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
        )

if __name__ == "__main__":
    unittest.main()