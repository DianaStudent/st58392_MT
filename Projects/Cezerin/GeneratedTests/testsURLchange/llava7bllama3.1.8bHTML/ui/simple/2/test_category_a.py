import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestHomepage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost")

    def tearDown(self):
        self.driver.quit()

    def test_homepage_components(self):
        # Home page headers
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        self.driver.find_element(By.XPATH, "//h1").is_displayed()
        
        # Category A links
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "category_a")))
        self.driver.find_elements(By.LINK_TEXT, "category_a")[0].is_displayed()
        
        # Category A1 link
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/home/category_a/category_a_1']")))
        self.driver.find_element(By.XPATH, "//a[@href='/home/category_a/category_a_1']").is_displayed()
        
        # Form fields
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        self.driver.find_element(By.NAME, "username").is_displayed()
        
        # Buttons
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").is_displayed()

if __name__ == "__main__":
    unittest.main()