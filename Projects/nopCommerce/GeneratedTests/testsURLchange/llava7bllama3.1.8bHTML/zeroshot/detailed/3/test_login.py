import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(html_data["home_before_login"])

    def test_login(self):
        # Click the "Login" button in the top navigation
        login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']//button[@type='button'][normalize-space()='Log in']"))
        )
        login_button.click()

        # Wait until the login page loads fully
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "Email"))
        )

        # Fill in the email and password fields using the provided credentials.
        email_input.send_keys("admin@admin.com")
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='Password']"))
        )
        password_input.send_keys("admin")

        # Click the login button.
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 login-button'][normalize-space()='Log in']"))
        )
        login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='admin-header-links']//a[normalize-space()='Administration']"))
        )
        self.assertTrue(logout_button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()