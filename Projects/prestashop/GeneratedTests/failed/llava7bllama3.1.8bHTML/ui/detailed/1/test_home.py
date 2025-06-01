from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShop(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("http://localhost:8080/en/")
        
        # Check header presence and visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header']")))
        
        # Check navigation menu presence and visibility
        nav_menu = self.driver.find_element(By.XPATH, "//ul[@class='nav-list']")
        self.assertTrue(nav_menu.is_displayed())
        
        # Check login link presence and visibility
        login_link = self.driver.find_element(By.XPATH, "//a[@href='/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")
        self.assertTrue(login_link.is_displayed())

    def test_clothes_page(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        
        # Check header presence and visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header']")))
        
        # Check breadcrumbs presence and visibility
        breadcrumbs = self.driver.find_element(By.XPATH, "//ul[@class='breadcrumb']")
        self.assertTrue(breadcrumbs.is_displayed())
        
        # Check product list presence
        products_list = self.driver.find_element(By.XPATH, "//div[@id='product-list']")
        self.assertTrue(products_list.is_displayed())

    def test_login_page(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        
        # Check header presence and visibility
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header']")))
        
        # Check form fields presence
        username_input = self.driver.find_element(By.XPATH, "//input[@id='username']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        self.assertTrue(username_input.is_displayed())
        self.assertTrue(password_input.is_displayed())

if __name__ == "__main__":
    unittest.main()