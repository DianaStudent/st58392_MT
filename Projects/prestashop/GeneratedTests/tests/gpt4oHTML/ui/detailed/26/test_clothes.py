import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/3-clothes")  # Load the clothes page

    def test_ui_elements(self):
        driver = self.driver

        # Wait and check for header visibility
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "header"))
        )
        self.assertIsNotNone(header, "Header is missing or not visible.")

        # Wait and check for footer visibility
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "footer"))
        )
        self.assertIsNotNone(footer, "Footer is missing or not visible.")

        # Wait and check for navigation visibility
        nav = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-nav"))
        )
        self.assertIsNotNone(nav, "Navigation is missing or not visible.")

        # Check the presence and visibility of input fields and buttons
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']"))
        )
        self.assertIsNotNone(search_input, "Search input is missing or not visible.")

        subscribe_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='submit'][value='Subscribe']"))
        )
        self.assertIsNotNone(subscribe_button, "Subscribe button is missing or not visible.")
        
        # Interact with the search input (as an example of a key interaction)
        search_input.click()
        search_input.send_keys('t-shirt')

        # Check that no required UI element is missing
        self.check_ui_elements()

    def check_ui_elements(self):
        driver = self.driver

        # Create a list of elements to check
        elements_to_check = [
            (By.ID, "header"),
            (By.ID, "footer"),
            (By.CLASS_NAME, "header-nav"),
            (By.CSS_SELECTOR, "input[aria-label='Search']"),
            (By.CSS_SELECTOR, "input[type='submit'][value='Subscribe']"),
            # Add more elements if needed
        ]

        # Check that these elements exist and are visible
        for by, value in elements_to_check:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((by, value))
                )
                self.assertIsNotNone(element, f"Element with locator ({by}, {value}) is missing or not visible.")
            except Exception as e:
                self.fail(f"Element with locator ({by}, {value}) is missing. Exception: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()