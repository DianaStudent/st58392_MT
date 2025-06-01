from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check navigation links
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
        except:
            self.fail("Clothes link is not visible")

        try:
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
        except:
            self.fail("Accessories link is not visible")

        try:
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Art link is not visible")
        
        # Check login and register links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes']")))
        except:
            self.fail("Login link is not visible")

        try:
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Register link is not visible")

        # Check product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is not visible")

        # Check search bar
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']")))
        except:
            self.fail("Search bar is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()