from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_structure_and_interaction(self):
        # Step 1: Load the page
        self.driver.get("http://max/login?returnUrl=%2F")

        # Step 1: Ensure structural elements are visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertIsNotNone(header, "Header is missing from the page.")
        self.assertIsNotNone(footer, "Footer is missing from the page.")

        # Step 2: Check presence and visibility of input fields, buttons, labels
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        self.assertIsNotNone(email_input, "Email input is missing from the page.")
        
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        self.assertIsNotNone(password_input, "Password input is missing from the page.")
        
        login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
        self.assertIsNotNone(login_button, "Login button is missing from the page.")

        register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
        self.assertIsNotNone(register_button, "Register button is missing from the page.")
        
        search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertIsNotNone(search_input, "Search input is missing from the page.")
        
        search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        self.assertIsNotNone(search_button, "Search button is missing from the page.")

        # Step 3: Interact with key UI elements
        search_input.send_keys("test")
        search_button.click()

        # Step 4: Confirm UI reacts visually (e.g., redirects to search page)
        self.wait.until(EC.url_contains("http://max/search"))
        current_url = self.driver.current_url
        self.assertIn("search?q=test", current_url, "Search did not navigate to the expected URL.")

        # Step 5: Assert that no required UI element is missing
        required_elements = [header, footer, email_input, password_input, login_button, register_button, search_input, search_button]
        for elem in required_elements:
            if not elem.is_displayed():
                self.fail(f"Required element {elem} is not visible on the page.")

    def tearDown(self):
        # Quit the browser session
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()