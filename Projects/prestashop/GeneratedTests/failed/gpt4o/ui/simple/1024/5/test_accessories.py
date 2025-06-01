from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
    
    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Wait for and check the presence of the header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check presence and visibility of main navigation links
            nav_links = [
                ("Home", "http://localhost:8080/en/"),
                ("Clothes", "http://localhost:8080/en/3-clothes"),
                ("Accessories", "http://localhost:8080/en/6-accessories"),
                ("Art", "http://localhost:8080/en/9-art")
            ]
            
            for name, link in nav_links:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '{link}')]"))
                )
                self.assertTrue(element.is_displayed(), f"Link '{name}' is not visible")

            # Check presence and visibility of 'Sign in' and 'Register' links
            signin = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/en/login')]"))
            )
            self.assertTrue(signin.is_displayed(), "Sign in link is not visible")
            
            register = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/en/registration')]"))
            )
            self.assertTrue(register.is_displayed(), "Register link is not visible")
            
            # Check presence and visibility of the search input
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "s"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
            
            # Check presence and visibility of the products section
            products_section = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "products"))
            )
            self.assertTrue(products_section.is_displayed(), "Products section is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()