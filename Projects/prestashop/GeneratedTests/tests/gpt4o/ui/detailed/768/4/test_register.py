import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header visibility
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed())

            # Check footer visibility
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed())

            # Check navigation visibility
            nav = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "nav")))
            self.assertTrue(nav.is_displayed())

            # Form fields
            fields = [
                (By.ID, "field-firstname"),
                (By.ID, "field-lastname"),
                (By.ID, "field-email"),
                (By.ID, "field-password"),
                (By.ID, "field-birthday")
            ]
            
            for by, value in fields:
                field = wait.until(EC.visibility_of_element_located((by, value)))
                self.assertTrue(field.is_displayed())

            # Checkboxes
            checkboxes = [
                (By.NAME, "optin"),
                (By.NAME, "psgdpr"),
                (By.NAME, "newsletter"),
                (By.NAME, "customer_privacy"),
            ]

            for by, value in checkboxes:
                checkbox = wait.until(EC.visibility_of_element_located((by, value)))
                self.assertTrue(checkbox.is_displayed())

            # Buttons
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
            self.assertTrue(save_button.is_displayed())

            # Interact with a UI element
            save_button.click()

            # Confirm that UI reacts (e.g., no essential element disappears)
            self.assertTrue(save_button.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to a missing or non-functional element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()