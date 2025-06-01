import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/registration')
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_visibility(self):
        try:
            # Check header
            header = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'header'))
            )
            
            # Check form fields
            gender_mr = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-id_gender-1'))
            )
            gender_mrs = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-id_gender-2'))
            )
            first_name = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-firstname'))
            )
            last_name = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-lastname'))
            )
            email = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-email'))
            )
            password = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-password'))
            )
            birthday = self.wait.until(
                EC.visibility_of_element_located((By.ID, 'field-birthday'))
            )

            # Check checkboxes
            optin_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.NAME, 'optin'))
            )
            psgdpr_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.NAME, 'psgdpr'))
            )
            newsletter_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.NAME, 'newsletter'))
            )
            customer_privacy_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.NAME, 'customer_privacy'))
            )

            # Check save button
            save_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-link-action="save-customer"]'))
            )

        except Exception as e:
            self.fail(f"Test failed due to missing element or timeout: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()