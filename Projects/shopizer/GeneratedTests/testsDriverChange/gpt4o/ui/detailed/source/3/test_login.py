import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver

        try:
            # Wait for header to be visible
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
            )
            self.assertIsNotNone(header, "Header is not present or visible.")

            # Wait for footer to be visible
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area"))
            )
            self.assertIsNotNone(footer, "Footer is not present or visible.")

            # Check navigation links
            nav_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a"))
            )
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are present.")

            # Check login form fields
            username_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
            self.assertIsNotNone(username_field, "Username field is not present or visible.")
            self.assertIsNotNone(password_field, "Password field is not present or visible.")

            # Check login button presence
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
            )
            self.assertIsNotNone(login_button, "Login button is not present or visible.")

            # Interact with the login button
            login_button.click()

            # Check for UI reaction (e.g., error message or redirect)
            # Placeholder: Checking if we possibly return to the login page.
            current_url = WebDriverWait(driver, 20).until(
                EC.url_contains("/login")
            )
            self.assertTrue(current_url, "No visible reaction after clicking login button.")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

if __name__ == "__main__":
    unittest.main()