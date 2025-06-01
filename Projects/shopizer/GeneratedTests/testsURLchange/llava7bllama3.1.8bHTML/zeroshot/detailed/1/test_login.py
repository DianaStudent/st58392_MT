import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Click on the account icon/button in the top-right
        account_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='account-btn']"))
        )
        account_icon.click()

        # Wait for the dropdown and click the "Login" link
        login_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Login')]"))
        )
        login_link.click()

        # Wait for the login form to appear
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )

        # Fill in the username and password fields using credentials
        username_field.send_keys("test2@user.com")
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("test**11")

        # Click the login button
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Wait for redirection or page update
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("/my-account")
        )

        # Confirm successful login by verifying that the current URL contains "/my-account"
        self.assertIn("/my-account", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()