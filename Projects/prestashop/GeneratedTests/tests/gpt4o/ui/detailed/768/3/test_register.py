import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence_and_visibility(self):
        driver = self.driver
        
        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except Exception as e:
            self.fail(f"Header not visible: {e}")
        
        # Check footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except Exception as e:
            self.fail(f"Footer not visible: {e}")

        # Check main form elements
        try:
            form = self.wait.until(EC.visibility_of_element_located((By.ID, 'customer-form')))
            fields = ['field-firstname', 'field-lastname', 'field-email', 'field-password', 'field-birthday']
            for field in fields:
                self.assertTrue(form.find_element(By.ID, field), f"{field} not found")
        except Exception as e:
            self.fail(f"Form elements not visible: {e}")

        # Check buttons
        try:
            save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
            newsletter_checkbox = form.find_element(By.NAME, 'newsletter')
            newsletter_checkbox.click()
            save_button.click()
        except Exception as e:
            self.fail(f"Buttons or interactions failed: {e}")

        # Check if feedback appears after clicking save (example UI reaction check)
        try:
            notification = self.wait.until(EC.visibility_of_element_located((By.ID, 'notifications')))
            self.assertTrue(notification.is_displayed(), "Notification after save not displayed")
        except Exception as e:
            self.fail(f"UI feedback check failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()