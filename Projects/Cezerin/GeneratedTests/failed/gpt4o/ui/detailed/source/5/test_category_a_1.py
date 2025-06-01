from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPageUI(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is missing")

        # Check for footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check for navigation links
        nav_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav")))
        self.assertIsNotNone(nav_links, "Navigation links are missing")

        # Check for search input field
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        self.assertIsNotNone(search_input, "Search input field is missing")

        # Check for sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
        self.assertIsNotNone(sort_dropdown, "Sort dropdown is missing")

        # Check for "Your cart is empty" text
        cart_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mini-cart p")))
        self.assertEqual(cart_text.text, "Your cart is empty", "'Your cart is empty' text is missing")

        # Interact with the sort dropdown
        sort_dropdown.click()
        sort_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='-date_created']")))
        sort_option.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()