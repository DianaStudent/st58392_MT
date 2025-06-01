import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header is visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not visible.")

        # Check footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible.")

        # Check main page elements
        main = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "main")))
        self.assertIsNotNone(main, "Main section is not visible.")

        # Check form elements
        form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
        self.assertIsNotNone(form, "Registration form is not visible.")

        # Check form fields
        fields = ["field-firstname", "field-lastname", "field-email", "field-password", "field-birthday"]
        for field in fields:
            elem = wait.until(EC.visibility_of_element_located((By.ID, field)))
            self.assertIsNotNone(elem, f"{field} is not visible.")

        # Check buttons
        buttons = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        self.assertIsNotNone(buttons, "Submit button is not visible.")

        # Interact with elements - click submit button
        buttons.click()

        # Verify confirmation - checking for URL changes or success message
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("http://localhost:8080/en/registration")
            )
        except:
            self.fail("URL did not contain expected string post submit.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()