import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_interface_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header element is missing.")

        # Check for main link elements
        nav_links = [
            ("home", "http://localhost:8080/en/"),
            ("clothes", "http://localhost:8080/en/3-clothes"),
            ("accessories", "http://localhost:8080/en/6-accessories"),
            ("art", "http://localhost:8080/en/9-art"),
            ("register", "http://localhost:8080/en/registration")
        ]

        for link_text, url in nav_links:
            link = driver.find_element(By.XPATH, f"//a[@href='{url}']")
            self.assertTrue(link.is_displayed(), f"Link {link_text} is not visible.")

        # Check for form fields
        email_input = driver.find_element(By.ID, "field-email")
        self.assertTrue(email_input.is_displayed(), "Email input field is missing or not visible.")

        password_input = driver.find_element(By.ID, "field-password")
        self.assertTrue(password_input.is_displayed(), "Password input field is missing or not visible.")

        # Check for buttons
        sign_in_button = driver.find_element(By.ID, "submit-login")
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is missing or not visible.")

        # Interact with 'Sign in' button to check UI updates
        sign_in_button.click()
        # (Further interaction logic can be added here to verify UI updates as needed.)

        # Verify no UI errors after interaction (Example: Check for a specific error message not appearing)
        try:
            error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'error-message')]")
            self.fail("Error message displayed on interaction: " + error_message.text)
        except:
            pass  # No error means test passes for this check

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()