from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/6-accessories")
        
        try:
            # Check navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check user account functionalities
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Check search bar
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Check category description
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-description")))

            # Check product list
            self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))

            # Check a button and interact with it
            button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-unstyle.select-title")))
            button.click()
            
            # Ensure the dropdown is shown after clicking the button
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-menu")))

        except Exception as e:
            self.fail(f"An element is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()