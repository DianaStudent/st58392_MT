from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_clothes_page_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Check header is visible
            header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            self.assertIsNotNone(header, "Header is missing.")

            # Check footer is visible
            footer = wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
            self.assertIsNotNone(footer, "Footer is missing.")

            # Check navigation menu
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.top-menu li a")))
            self.assertGreaterEqual(len(nav_links), 3, "Main navigation links are missing.")

            # Check search input field
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            self.assertIsNotNone(search_input, "Search input is missing.")

            # Check "Sign in" link
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertIsNotNone(sign_in_link, "Sign in link is missing.")

            # Check "Subscribe" button in the newsletter section
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter']")))
            self.assertIsNotNone(subscribe_button, "Subscribe button is missing.")

            # Interact with Search Bar
            search_input.send_keys("shirt")
            
            # Interact with Subscribe
            subscribe_button.click()

            # Verify Category section visibility
            category_header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
            self.assertIsNotNone(category_header, "Category header is missing.")

            # Assert product list is not empty
            products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.js-product")))
            self.assertGreaterEqual(len(products), 1, "No products found on the page.")

        except Exception as e:
            self.fail(f"Test failed due to missing or invisible elements: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()