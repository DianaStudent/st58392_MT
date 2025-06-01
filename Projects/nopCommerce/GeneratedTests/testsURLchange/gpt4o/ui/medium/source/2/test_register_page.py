import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/register?returnUrl=%2F')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Confirm presence of navigation links
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-links a.ico-register')))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-links a.ico-login')))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-links a.ico-wishlist')))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-links a.ico-cart')))
        except Exception as e:
            self.fail(f"Navigation link test failed: {e}")

        # Confirm presence of registration form elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'FirstName')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'LastName')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'ConfirmPassword')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
        except Exception as e:
            self.fail(f"Form element test failed: {e}")

        # Interact with elements
        try:
            newsletter_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, 'Newsletter')))
            newsletter_checkbox.click()

            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
            register_button.click()

            # Confirm that some UI update happened without errors
            self.wait.until(EC.presence_of_element_located((By.ID, 'dialog-notifications-error')))
            error_dialog = driver.find_element(By.ID, 'dialog-notifications-error')
            self.assertFalse(error_dialog.is_displayed(), "Error dialog should not be displayed.")
        except Exception as e:
            self.fail(f"Element interaction or visual update check failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()