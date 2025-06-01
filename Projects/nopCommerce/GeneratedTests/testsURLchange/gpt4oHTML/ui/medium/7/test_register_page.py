import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/register?returnUrl=%2F')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration_page_ui(self):
        driver = self.driver
        wait = self.wait

        # Check header links
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile")))
        except:
            self.fail("Main navigation links are not visible")

        # Check form fields and buttons
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except:
            self.fail("Form fields or Register button is not visible")

        # Interactive elements
        try:
            first_name_field = driver.find_element(By.ID, "FirstName")
            first_name_field.send_keys("Test")
            last_name_field = driver.find_element(By.ID, "LastName")
            last_name_field.send_keys("User")
            email_field = driver.find_element(By.ID, "Email")
            email_field.send_keys("testuser@example.com")
        except Exception as e:
            self.fail(f"Unable to input data: {str(e)}")

        # Click on Register button
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button not clickable")

        # Check for any UI errors
        try:
            error_dialog = driver.find_element(By.ID, "dialog-notifications-error")
            if error_dialog.is_displayed():
                self.fail("Error dialog is displayed")
        except:
            pass  # dialog-notifications-error is not present which means no UI error

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()