from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_UI_elements(self):
        driver = self.driver
        
        # Check for the header links: Home, Clothes, Accessories, Art
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except:
            self.fail("Header links are missing or not visible")
        
        # Check for the sign in button
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in link is missing or not visible")
        
        # Check for the search bar
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search bar is missing or not visible")
        
        # Check for the breadcrumb navigation: Home > Clothes
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb a[href='/en/']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb span")))
        except:
            self.fail("Breadcrumb navigation is missing or not visible")

        # Check for the product list
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is missing or not visible")
        
        # Check for the footer link: Subscribe button
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Subscribe']")))
        except:
            self.fail("Subscribe button in footer is missing or not visible")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()