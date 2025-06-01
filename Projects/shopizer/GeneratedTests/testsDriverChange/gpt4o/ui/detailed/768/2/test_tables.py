from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertIsNotNone(header, "Header is missing or not visible.")

        # Check navigation links visibility
        nav_links = driver.find_elements(By.CSS_SELECTOR, "nav ul li a")
        self.assertEqual(len(nav_links), 3, "Not all navigation links are visible.")
        
        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertIsNotNone(footer, "Footer is missing or not visible.")

        # Check 'Accept cookies' button and interact
        accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(accept_cookies_button, "Accept cookies button is missing or not clickable.")
        accept_cookies_button.click()

        # Check product add-to-cart buttons
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, ".pro-cart button")
        self.assertEqual(len(add_to_cart_buttons), 4, "Not all 'Add to cart' buttons are visible.")
        
        # Interact with a product's add-to-cart button
        add_to_cart_buttons[0].click()
        
        # Check login link visibility
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertIsNotNone(login_link, "Login link is missing or not visible.")
        
        # Check register link visibility
        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link, "Register link is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()