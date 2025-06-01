import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login(self):
        # Open the home page
        self.driver.get("http://localhost:8000/dk")

        # Click the "Account" link
        account_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/account']")))
        account_link.click()

        # Wait for the login page to load
        login_page_loaded = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "login-form")))

        # Enter email and password
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys("user@test.com")

        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys("testuser")

        # Click the sign-in button
        signin_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        signin_button.click()

        # Verify that the welcome message is present
        welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='welcome-message']")))
        self.assertEqual(welcome_message.text, "Welcome to...")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()