import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoPage(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # 1. Check that structural elements are visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except Exception:
            self.fail("Structural elements are missing")

        # 2. Check presence and visibility of input fields, buttons, labels, and sections
        try:
            # Search bar
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            search_input = search_widget.find_element(By.NAME, "s")
            self.assertTrue(search_input.is_displayed(), "Search input field is not visible.")

            # Language selector
            language_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Language dropdown']")))
            self.assertIsNotNone(language_button, "Language dropdown button is missing.")

            # Login link
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible.")
            
            # Register link
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible.")

        except Exception:
            self.fail("Input fields, buttons, labels, or sections are missing")

        # 3. Interact with key UI elements and confirm visual reaction
        try:
            # Click the language button to open the dropdown
            language_button.click()
            language_options = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu")))
            self.assertTrue(language_options.is_displayed(), "Language dropdown did not open.")

            # Click the login link to navigate to login page
            login_link.click()
            wait.until(EC.url_contains("login"))
            self.assertIn("login", driver.current_url, "Failed to navigate to login page.")

            # Go back to home
            driver.back()

        except Exception:
            self.fail("UI interaction failed")

    def tearDown(self):
        # Close the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()