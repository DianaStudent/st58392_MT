import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        # Check the presence of the main UI components

        # Header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header element not found or not visible")

        # Contact us link
        try:
            contact_link = self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_contact_link')))
        except:
            self.fail("Contact us link element not found or not visible")

        # Language Selector
        try:
            language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_language_selector')))
        except:
            self.fail("Language selector element not found or not visible")

        # User info for login
        try:
            user_info = self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_user_info')))
        except:
            self.fail("User info element (for login) not found or not visible")

        # Cart information
        try:
            cart = self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_cart')))
        except:
            self.fail("Cart element not found or not visible")

        # Top menu for navigation
        try:
            top_menu = self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_top_menu')))
        except:
            self.fail("Top menu element not found or not visible")

        # Search widget
        try:
            search_widget = self.wait.until(EC.visibility_of_element_located((By.ID, 'search_widget')))
        except:
            self.fail("Search widget element not found or not visible")

        # Category block
        try:
            category_block = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'block-category')))
        except:
            self.fail("Category block element not found or not visible")

        # Products list
        try:
            products_list = self.wait.until(EC.visibility_of_element_located((By.ID, 'products')))
        except:
            self.fail("Products list element not found or not visible")

        # Footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except:
            self.fail("Footer element not found or not visible")

if __name__ == "__main__":
    unittest.main()