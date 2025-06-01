from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver

        # Verify the visibility of the header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header is not visible on the page.")

        # Verify the visibility of the footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except:
            self.fail("Footer is not visible on the page.")

        # Verify the visibility of the navigation menu
        try:
            nav_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-nav')))
        except:
            self.fail("Navigation menu is not visible.")

        # Verify the presence of search field
        try:
            search_field = self.wait.until(EC.visibility_of_element_located((By.NAME, 's')))
        except:
            self.fail("Search field is not visible.")

        # Verify button and links visibility
        try:
            contact_us = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sign in')))
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping-cart')))
        except:
            self.fail("One of the key buttons/links (Contact us, Sign in, Cart) is not visible.")

        # Click the 'Cart' icon to ensure it is interactive
        try:
            cart_button.click()
        except:
            self.fail("Unable to interact with the Cart button.")

        # Confirm visual reaction of the UI after interaction
        try:
            cart_products_count = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-products-count')))
        except:
            self.fail("Cart products count not visible after clicking the Cart button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()