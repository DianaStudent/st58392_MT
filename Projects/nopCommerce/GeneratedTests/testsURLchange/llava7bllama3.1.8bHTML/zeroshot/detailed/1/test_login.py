import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(html_data["home_before_login"])

    def test_login(self):
        # 1. Click the "Login" button in the top navigation
        login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main > .page.login-page > .buttons > button.button-1.login-button"))
        )
        login_button.click()

        # 2. Wait until the login page loads fully.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".customer-blocks")))

        # 3. Fill in the email and password fields using the provided credentials
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.email"))
        )
        email_field.send_keys("admin@admin.com")

        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        password_field.send_keys("admin")

        # 4. Click the login button
        login_button.click()

        # 5. Verify that the user is logged in by checking the "Log out" button is present in the top navigation.
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".admin-header-links > a.administration"))
        )
        self.assertEqual("Administration", logout_button.text)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()