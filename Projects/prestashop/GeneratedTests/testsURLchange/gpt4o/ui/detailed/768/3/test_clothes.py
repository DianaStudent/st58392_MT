import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Check for header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header is missing")

        # Check for footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except:
            self.fail("Footer is missing")
        
        # Check for search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        except:
            self.fail("Search input is missing")

        # Check for categories
        try:
            categories = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'block-categories')))
        except:
            self.fail("Categories are missing")
        
        # Check for products section
        try:
            products_section = self.wait.until(EC.visibility_of_element_located((By.ID, 'products')))
        except:
            self.fail("Products section is missing")

        # Check for sign-in link
        try:
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Sign in')))
            sign_in_link.click()
        except:
            self.fail("Sign in link is missing or not clickable")

        # Check the page navigated to sign in
        try:
            sign_in_page = self.wait.until(EC.visibility_of_element_located((By.ID, 'login-form')))
        except:
            self.fail("Sign in page did not load")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()