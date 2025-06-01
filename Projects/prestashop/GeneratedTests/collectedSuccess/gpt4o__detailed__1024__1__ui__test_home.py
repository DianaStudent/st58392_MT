import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.url = "http://localhost:8080/en/"
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.url)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check navigation menu presence and visibility
        menu = wait.until(EC.visibility_of_element_located((By.ID, 'top-menu')))
        self.assertIsNotNone(menu, "Navigation menu is not visible")

        # Check search bar presence and visibility
        search_bar = wait.until(EC.visibility_of_element_located((By.NAME, 's')))
        self.assertIsNotNone(search_bar, "Search bar is not present or visible")

        # Check cart button presence and visibility
        cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping-cart')))
        self.assertIsNotNone(cart, "Cart button is not present or visible")

        # Check login link presence and visibility
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertIsNotNone(login_link, "Login link is not present or visible")

        # Check 'Popular Products' section presence
        popular_products_section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'products')))
        self.assertIsNotNone(popular_products_section, "Popular Products section is not visible")

        # Check if any product is present
        product = popular_products_section.find_elements(By.CLASS_NAME, 'product')
        self.assertTrue(len(product) > 0, "No products found in the Popular Products section")

        # Check 'Register' link presence and visibility
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
        self.assertIsNotNone(register_link, "Register link is not present or visible")

        # Interaction: Click on 'Sign in' link to verify it works
        login_link.click()
        login_page_header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        self.assertIsNotNone(login_page_header, "Failed to load the login page")

        # Assert for missing elements and actions
        if not header or not footer or not menu or not search_bar or not cart or not login_link:
            self.fail("One or more required UI elements are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()