from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class SimpleUITest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver and open the website
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for the page to load and check the header
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
            )
        except:
            self.fail("Header not found or not visible")

        # Check navigation links
        try:
            nav_links = driver.find_elements(By.CSS_SELECTOR, "nav ul li a")
            self.assertEqual(len(nav_links), 3, "Expected 3 navigation links")
        except:
            self.fail("Navigation links not found or not visible")

        # Verify existence and visibility of the login and register links
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
            )
        except:
            self.fail("Login or Register link not found or not visible")

        # Check for the existence of the shopping cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
        except:
            self.fail("Shopping cart button not found or not visible")

        # Interact with the "Accept cookies" button
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable")

        # Check for the product list
        try:
            product_list = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shop-area"))
            )
        except:
            self.fail("Product list not found or not visible")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()