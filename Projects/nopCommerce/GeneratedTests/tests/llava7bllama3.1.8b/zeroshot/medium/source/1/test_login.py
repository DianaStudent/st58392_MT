import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_login_medium_process(self):
        # Click the "Login" link
        login_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log In')]"))
        )
        login_link.click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "main"))
        )

        # Enter email and password
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))
        )
        email_input.send_keys("admin@admin.com")

        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
        )
        password_input.send_keys("admin")

        # Click the login button to submit the form
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present in the top navigation
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Administration')]"))
        )
        self.assertTrue(logout_button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()