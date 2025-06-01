from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Click the "Account" link
        account_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Account")))
        account_link.click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))

        # Enter the email and password
        self.driver.find_element(By.ID, "email").send_keys("user@test.com")
        self.driver.find_element(By.ID, "password").send_keys("testuser")

        # Click the sign-in button
        signin_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "signin")))
        signin_button.click()

        # Verify that the welcome message is present
        welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "welcome-message")))
        self.assertEqual(welcome_message.text, "Welcome to your account!")

if __name__ == '__main__':
    unittest.main()