from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run headless if preferred
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://max/")  # Use the actual URL for the login page

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for and check the presence of the Email input
        try:
            email_input = wait.until(EC.element_to_be_clickable((By.ID, "Email")))
        except:
            self.fail("Email input not found")

        # Enter email
        email_input.send_keys("admin@admin.com")

        # Wait for and check the presence of the Password input
        try:
            password_input = wait.until(EC.element_to_be_clickable((By.ID, "Password")))
        except:
            self.fail("Password input not found")

        # Enter password
        password_input.send_keys("admin")

        # Wait for and check the presence of the Log in button
        try:
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.login-button")))
        except:
            self.fail("Log in button not found")

        # Click Log in
        login_button.click()

        # Wait for and confirm the presence of the "Log out" button to confirm successful login
        try:
            logout_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/logout']")))
        except:
            self.fail("Log out button not found, login might not have been successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()