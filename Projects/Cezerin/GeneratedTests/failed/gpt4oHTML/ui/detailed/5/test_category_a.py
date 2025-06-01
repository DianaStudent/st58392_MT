from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCategorAUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://example.com/category-a")  # Replace with the appropriate URL

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header'))), "Header is missing")
        
        # Check footer
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer'))), "Footer is missing")
        
        # Check primary navigation
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav'))), "Primary navigation is missing")

        # Check mobile navigation
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mobile-nav'))), "Mobile navigation is missing")
        
        # Check search input field
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input'))), "Search input field is missing")
        
        # Check sort dropdown
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//select"))), "Sort dropdown is missing")
        
        # Check the category title
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title'))), "Category title is missing")
        
        # Check Product A
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product A'))), "Product A link is missing")

        # Check buttons (like cart and filter products)
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button'))), "Cart button is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'button'))), "Filter products button is missing")
        
        # Interact with cart button, only verifying there is no exception.
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'cart-button')))
        cart_button.click()

        # Confirm that the mini-cart section is visible
        mini_cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mini-cart')))
        self.assertTrue(mini_cart.is_displayed(), "Mini-cart section didn't appear.")
        
        # Check all main UI components exist and visible
        for locator_by, locator_value, element_name in [
            (By.TAG_NAME, 'header', "Header"),
            (By.CLASS_NAME, 'footer', "Footer"),
            (By.CLASS_NAME, 'primary-nav', "Primary Navigation"),
            (By.CLASS_NAME, 'mobile-nav', "Mobile Navigation"),
            (By.CLASS_NAME, 'search-input', "Search Input Field"),
            (By.CLASS_NAME, 'cart-button', "Cart Button"),
            (By.CLASS_NAME, 'button', "Filter Button"),
            (By.CLASS_NAME, 'category-title', "Category Title"),
            (By.LINK_TEXT, 'Product A', "Product A Link"),
            (By.XPATH, "//select", "Sort Dropdown")
        ]:
            self.assertTrue(wait.until(EC.visibility_of_element_located((locator_by, locator_value))), f"{element_name} is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()