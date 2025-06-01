import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Verify header elements
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Verify navigation links
            home_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            self.assertIsNotNone(home_link)

            clothes_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            self.assertIsNotNone(clothes_link)

            accessories_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
            )
            self.assertIsNotNone(accessories_link)

            # Verify form fields on registration form
            firstname_field = self.wait.until(
                EC.visibility_of_element_located((By.ID, "field-firstname"))
            )
            self.assertIsNotNone(firstname_field)

            lastname_field = self.wait.until(
                EC.visibility_of_element_located((By.ID, "field-lastname"))
            )
            self.assertIsNotNone(lastname_field)

            email_field = self.wait.until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            self.assertIsNotNone(email_field)

            password_field = self.wait.until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )
            self.assertIsNotNone(password_field)

            # Verify checkboxes
            optin_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "optin"))
            )
            self.assertIsNotNone(optin_checkbox)

            privacy_checkbox = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "psgdpr"))
            )
            self.assertIsNotNone(privacy_checkbox)

            # Verify submit button
            submit_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
            )
            self.assertIsNotNone(submit_button)
            
        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()