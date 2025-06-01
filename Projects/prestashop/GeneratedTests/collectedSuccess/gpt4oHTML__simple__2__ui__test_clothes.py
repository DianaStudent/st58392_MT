import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or visible.")
        
        # Check category links in header
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except:
            self.fail("Category links are not present or visible in header.")
        
        # Check main content area
        try:
            main_content = wait.until(EC.visibility_of_element_located((By.ID, "content-wrapper")))
        except:
            self.fail("Main content area is not present or visible.")
        
        # Check search widget
        try:
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            search_input = search_widget.find_element(By.CSS_SELECTOR, "input[name='s']")
        except:
            self.fail("Search widget or its input field is not present or visible.")

        # Check login link
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Login link is not present or visible.")

        # Check registration link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
        except:
            self.fail("Registration link is not present or visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()