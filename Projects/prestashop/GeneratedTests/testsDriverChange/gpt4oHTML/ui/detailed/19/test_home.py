import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        
    def test_ui_structure(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the visibility of the header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is missing")
        
        # Check the visibility of the footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check the visibility of the navbar
        navbar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertIsNotNone(navbar, "Navigation bar is missing")

        # Check the visibility of the input fields, buttons, and sections
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertIsNotNone(search_input, "Search input field is missing")

        subscribe_button = wait.until(EC.visibility_of_element_located((By.NAME, "submitNewsletter")))
        self.assertIsNotNone(subscribe_button, "Subscribe button is missing")

        # Check the links in the top menu
        clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
        accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
        art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        
        self.assertIsNotNone(clothes_link, "Clothes link is missing")
        self.assertIsNotNone(accessories_link, "Accessories link is missing")
        self.assertIsNotNone(art_link, "Art link is missing")

        # Interact with the key UI elements
        art_link.click()
        
        # Confirm that the UI reacts visually
        page_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "title"))).get_attribute("textContent")
        self.assertIn("Art", driver.title, "Navigating to the Art page was unsuccessful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()