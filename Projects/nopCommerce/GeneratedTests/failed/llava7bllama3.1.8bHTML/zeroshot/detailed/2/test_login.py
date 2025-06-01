from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        # Open the home page.
        self.driver.get(html_data['home_before_login'])

        # Click the "Login" button in the top navigation.
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login')]"))).click()

        # Wait until the login page loads fully.
        self.login_page_loaded = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='__RequestVerificationToken']")))

        # Fill in the email and password fields using the provided credentials.
        self.email_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Email')))
        self.password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))

        self.email_field.send_keys('admin@admin.com')
        self.password_field.send_keys('admin')

        # Click the login button.
        self.login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-button')))
        self.login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        try:
            log_out_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log out')))
            self.fail('Login successful')
        except TimeoutException:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()