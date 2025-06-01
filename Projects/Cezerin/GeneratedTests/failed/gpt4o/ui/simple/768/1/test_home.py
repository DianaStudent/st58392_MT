from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for main logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image")))
        except:
            self.fail("Logo is not present or not visible")

        # Check for Categories in nav bar
        try:
            category_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            category_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            category_c = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
        except:
            self.fail("Categories in the navigation bar are missing or not visible")

        # Check for Search bar
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        except:
            self.fail("Search input is not present or not visible")

        # Check for Cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img")))
        except:
            self.fail("Cart button is not present or not visible")

        # Check for Best Sellers section
        try:
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4.has-text-centered")))
        except:
            self.fail("Best Sellers section is not present or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()