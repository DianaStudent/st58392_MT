import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUITestCase(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome web driver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for main UI elements presence
        try:
            wait.until(EC.presence_of_element_located((By.ID, "header")))
            wait.until(EC.presence_of_element_located((By.ID, "login-form")))
            wait.until(EC.presence_of_element_located((By.ID, "wrapper")))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer.js-footer")))
        except:
            self.fail("Main UI components are missing.")

        # Check if all expected links are present and visible
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in to your customer account")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("Key navigation links are missing or not visible.")

        # Interact with an element
        try:
            sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_button.click()

            # After clicking, verify that we navigated to the sign-in page
            current_url = driver.current_url
            self.assertIn("login", current_url, "Failed to navigate to login page.")
        except:
            self.fail("Failed to interact with Sign in button.")

        # Check if any other unexpected errors occurred in the UI during the process
        page_source = driver.page_source
        self.assertNotIn("error", page_source.lower(), "Errors found in UI.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()