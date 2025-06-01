from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header visibility
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not visible.")

        # Check for footer visibility
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer not visible.")

        # Check for navigation links
        links = [
            ("Home", "http://localhost:8080/en/"),
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
            ("Sign in", "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"),
            ("Create account", "http://localhost:8080/en/registration")
        ]
        
        for text, url in links:
            try:
                link_element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))
                self.assertEqual(link_element.get_attribute("href"), url)
            except:
                self.fail(f"Link with text '{text}' not visible or wrong URL.")

        # Check for search input field
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input field not visible.")

        # Check for search button (icon)
        try:
            search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search")))
        except:
            self.fail("Search button not visible.")
        
        # Interact with a key element, such as the search form
        try:
            search_input.send_keys("framed poster")
            search_button.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Failed to interact with search form or verify result visibility.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()