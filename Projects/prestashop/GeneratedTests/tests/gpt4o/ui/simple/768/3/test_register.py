import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        # Setting up Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header title
        header_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.page-header h1')))
        self.assertEqual(header_title.text, "Create an account")

        # Check form fields
        expected_fields = [
            (By.ID, "field-id_gender-1"),  # Mr.
            (By.ID, "field-id_gender-2"),  # Mrs.
            (By.ID, "field-firstname"),
            (By.ID, "field-lastname"),
            (By.ID, "field-email"),
            (By.ID, "field-password"),
            (By.ID, "field-birthday"),
            (By.NAME, "optin"),
            (By.NAME, "psgdpr"),
            (By.NAME, "newsletter"),
            (By.NAME, "customer_privacy"),
        ]

        for selector in expected_fields:
            try:
                element = wait.until(EC.visibility_of_element_located(selector))
                self.assertTrue(element.is_displayed())
            except Exception:
                self.fail(f"Element with selector {selector} is not visible.")

        # Check submit button
        save_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-footer .btn-primary")))
        self.assertTrue(save_button.is_displayed())

    def tearDown(self):
        # Closing the browser after test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()