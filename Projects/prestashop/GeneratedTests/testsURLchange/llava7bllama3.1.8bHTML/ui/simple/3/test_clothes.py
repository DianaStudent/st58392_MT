import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_homepage(self):
        self.driver.get("http://localhost:8080/en/")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='nav-list']/li[1]")))
        
    def test_clothes_page(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='product_list']/li[1]")))

    def test_accessories_page(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='product_list']/li[1]")))

    def test_art_page(self):
        self.driver.get("http://localhost:8080/en/9-art")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='product_list']/li[1]")))

    def test_login_page(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))

    def test_register_page(self):
        self.driver.get("http://localhost:8080/en/registration")
        
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))

if __name__ == '__main__':
    unittest.main()