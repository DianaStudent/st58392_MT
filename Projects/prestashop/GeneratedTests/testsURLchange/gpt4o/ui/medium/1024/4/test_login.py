import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check that the header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.page-header h1")))
        except:
            self.fail("Header not found or not visible.")

        # Check navigation links
        links = [
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art")
        ]
        
        for link_text, link_url in links:
            try:
                link_element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertEqual(link_element.get_attribute('href'), link_url)
            except:
                self.fail(f"Link {link_text} not found or not visible.")

        # Check form inputs
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Email or Password input not found or not visible.")

        # Check buttons
        try:
            submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#submit-login")))
        except:
            self.fail("Submit button not found or not visible.")

        # Interact with elements
        try:
            email_input.send_keys("test@example.com")
            password_input.send_keys("password")
            submit_button.click()

            # Verify the UI updates or transitions correctly
            wait.until(EC.title_contains("Account"))
        except:
            self.fail("Error during interaction with UI elements.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()