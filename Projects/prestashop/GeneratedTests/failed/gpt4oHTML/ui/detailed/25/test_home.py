from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Check if header is present and visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check if footer is present and visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer not found or not visible")

        # Check if navigation is present and visible
        try:
            nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation bar not found or not visible")

        # Check input fields, buttons and important links
        try:
            contact_us_link = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#contact-link a[href='http://localhost:8080/en/contact-us']")))
        except:
            self.fail("Contact us link not found or not visible")
        
        try:
            language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
        except:
            self.fail("Language selector not found or not visible")
        
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")))
        except:
            self.fail("Sign in button not found or not visible")

        try:
            search_input = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#search_widget input[name='s']")))
        except:
            self.fail("Search input not found or not visible")

        # Interact with some of the UI elements
        sign_in_button.click()
        self.assertEqual(driver.current_url, "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F")

        # Assert no required UI element is missing
        required_elements = [header, footer, nav, contact_us_link, language_selector, sign_in_button, search_input]
        for element in required_elements:
            self.assertTrue(element.is_displayed(), f"Element {element} is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()