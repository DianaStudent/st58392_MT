from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopperWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_ui_components(self):
        # Check header is present and visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='shopper']")))
        
        # Check search bar is present and visible
        search_bar = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        self.assertTrue(search_bar.is_enabled())
        
        # Check login button is present and visible
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Log In']")
        self.assertTrue(login_button.is_enabled())
        
        # Check navigation menu items are present and visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//nav//ul/li")))
        
    def test_tables_category(self):
        tables_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Tables']")))
        tables_link.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//h2[text()='Tables']//..//table")))
        
    def test_chairs_category(self):
        chairs_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Chairs']")))
        chairs_link.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//h2[text()='Chairs']//..//table")))
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()