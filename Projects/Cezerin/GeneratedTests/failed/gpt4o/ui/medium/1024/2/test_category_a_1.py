from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubcategoryPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get('http://localhost:3000/category-a-1')

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo-image')))
        except Exception as e:
            self.fail(f"Logo is not visible: {str(e)}")

        # Check navigation links
        nav_links = ['Category A', 'Category B', 'Category C']
        for link_text in nav_links:
            try:
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except Exception as e:
                self.fail(f"Navigation link '{link_text}' is not visible: {str(e)}")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        except Exception as e:
            self.fail(f"Search input is not visible: {str(e)}")

        # Check sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort select')))
            sort_dropdown.click()
        except Exception as e:
            self.fail(f"Sort dropdown is not visible or not clickable: {str(e)}")

        # Check if sort options exist
        sort_options = ['Favorite', 'Newest', 'Price low to high', 'Price high to low']
        for option_text in sort_options:
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, f"//option[text()='{option_text}']")))
            except Exception as e:
                self.fail(f"Sort option '{option_text}' is not visible: {str(e)}")

        # Check for an empty cart message
        try:
            cart_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Your cart is empty']")))
        except Exception as e:
            self.fail(f"Cart message is not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()