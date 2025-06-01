import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check main navigation links
        navbar_links = [
            (By.LINK_TEXT, "Clothes"),
            (By.LINK_TEXT, "Accessories"),
            (By.LINK_TEXT, "Art"),
        ]
        
        for locator in navbar_links:
            try:
                element = self.wait.until(EC.visibility_of_element_located(locator))
                self.assertTrue(element.is_displayed(), f"Element {locator[1]} is not visible.")
            except Exception as e:
                self.fail(f"Navigation link {locator[1]} not found or not visible: {e}")

        # Check login button
        try:
            login_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible.")
        except Exception as e:
            self.fail(f"Login button not found or not visible: {e}")

        # Check search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
        except Exception as e:
            self.fail(f"Search input not found or not visible: {e}")

        # Interact with a button
        try:
            login_button.click()
            self.wait.until(EC.url_contains("login"))
            self.assertIn("login", driver.current_url, "Failed to navigate to login page.")
        except Exception as e:
            self.fail(f"Interacting with the login button failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()