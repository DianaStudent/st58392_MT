import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Open the home page and click the "Login" button in the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        login_link.click()

        # Wait until the login page loads fully
        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))

        # Fill in the email and password fields using the provided credentials
        email_field.send_keys("admin@admin.com")
        password_field = driver.find_element(By.ID, "Password")
        password_field.send_keys("admin")

        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
        login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_button.is_displayed(), "Log out button should be visible after logging in.")
        except Exception as e:
            self.fail(f"Log out button not found after login, login process failed. Exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()