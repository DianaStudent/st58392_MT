from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("about:blank")  # Load a blank page initially

    def test_ui_elements(self):
        driver = self.driver
        driver.get("data:text/html;charset=utf-8,{html}".format(html=html_data["html"]))
        
        # Wait for the header to be visible
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'header'))
            )
        except:
            self.fail("Header not found or not visible.")

        # Ensure navigation links are present and visible
        try:
            nav_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav a'))
            )
        except:
            self.fail("Navigation links not found or not visible.")
        
        # Check the search input field
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input'))
            )
        except:
            self.fail("Search input field not found or not visible.")
        
        # Check sort select box
        try:
            sort_select = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.select select'))
            )
        except:
            self.fail("Sort select box not found or not visible.")

        # Check product elements
        try:
            product_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.products a'))
            )
        except:
            self.fail("Product links not found or not visible.")

        # Verify footer presence
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
            )
        except:
            self.fail("Footer not found or not visible.")

        # Interact with a product link
        try:
            product_links[0].click()
            WebDriverWait(driver, 20).until(
                EC.url_contains(product_links[0].get_attribute('href'))
            )
        except:
            self.fail("Product link interaction failed.")

        # Check mini-cart message
        try:
            cart_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-cart p'))
            )
            self.assertEqual(cart_message.text, "Your cart is empty")
        except:
            self.fail("Mini-cart message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()