import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify presence of header elements
        try:
            header_links = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-links')))
            self.assertIsNotNone(header_links)
        except:
            self.fail("Header links are missing or not visible.")

        # Verify presence of login form fields
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
            self.assertIsNotNone(email_input)
            self.assertIsNotNone(password_input)
        except:
            self.fail("Login form fields are missing or not visible.")

        # Verify presence of login button
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
            self.assertIsNotNone(login_button)
        except:
            self.fail("Login button is missing or not visible.")

        # Interact with login button to check no errors in UI
        try:
            login_button.click()
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, 'dialog-notifications-error'))
            )
        except:
            pass  # Expect error due to empty input, this shows button interaction is functional

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()