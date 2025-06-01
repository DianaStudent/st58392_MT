from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check for main sections and links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))).is_displayed()
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))).is_displayed()
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art"))).is_displayed()
        except:
            self.fail("One or more navigation links not found or not visible")

        # Check for login and register links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))).is_displayed()
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account"))).is_displayed()
        except:
            self.fail("Sign in or Create account links not found or not visible")

        # Check for search widget
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']")))
            search_input.is_displayed()
        except:
            self.fail("Search input not found or not visible")

        # Check for cart link
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))).is_displayed()
        except:
            self.fail("Shopping cart not found or not visible")

        # Check for popular products section
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products-section-title.text-uppercase"))).is_displayed()
        except:
            self.fail("Popular products section not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()