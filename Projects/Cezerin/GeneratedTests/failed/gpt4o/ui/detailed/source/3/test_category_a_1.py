from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        # Check header presence and visibility
        header = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is missing")

        # Check footer presence and visibility
        footer = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check navigation presence and visibility
        nav = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav')))
        self.assertIsNotNone(nav, "Navigation is missing")

        # Check search input presence and visibility
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        self.assertIsNotNone(search_input, "Search input is missing")

        # Check sort select dropdown presence and visibility
        sort_dropdown = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.select select')))
        self.assertIsNotNone(sort_dropdown, "Sort dropdown is missing")

        # Check cart button presence and visibility
        cart_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button')))
        self.assertIsNotNone(cart_button, "Cart button is missing")

        # Check breadcrumb presence and visibility
        breadcrumb = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
        self.assertIsNotNone(breadcrumb, "Breadcrumb is missing")

        # Check that clicking cart button opens mini cart
        cart_button.click()
        mini_cart = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-cart')))
        self.assertTrue(mini_cart.is_displayed(), "Mini cart is not visible after clicking cart button")

if __name__ == "__main__":
    unittest.main()