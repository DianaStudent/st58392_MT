import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SimpleSeleniumTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements_presence(self):
        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is not visible on the page")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible on the page")
        
        # Check logo
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a")))
        self.assertIsNotNone(logo, "Logo is missing or not visible")

        # Check main navigation links
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, ".main-menu a")
        self.assertGreater(len(nav_links), 0, "Main navigation links are not visible or missing")

        # Check Accept Cookies button
        cookie_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(cookie_btn, "Accept Cookies button is missing or not visible")

        # Interact with Accept Cookies button
        cookie_btn.click()

        # Check Featured Products section
        featured_section = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-area")))
        self.assertIsNotNone(featured_section, "Featured Products section is missing or not visible")

        # Check search input field
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        self.assertIsNotNone(search_field, "Email input field is missing or not visible")

        # Check Subscribe button
        subscribe_button = self.driver.find_element(By.CSS_SELECTOR, "button.button")
        self.assertIsNotNone(subscribe_button, "Subscribe button is missing or not visible")

        # Interact with Subscribe button
        subscribe_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()