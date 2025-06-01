import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check and click "My account" to go to login
        my_account = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        if my_account is None:
            self.fail("My account link is not present on the home page.")
        my_account.click()

        # Wait for the login page to load
        login_title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        if not login_title or login_title.text != "Welcome, Please Sign In!":
            self.fail("Login page did not load correctly.")

        # Fill login form
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        if email_input is None:
            self.fail("Email input field is not present on the login page.")
        email_input.send_keys("admin@admin.com")

        password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        if password_input is None:
            self.fail("Password input field is not present on the login page.")
        password_input.send_keys("admin")

        # Click login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]")))
        if login_button is None:
            self.fail("Login button is not present on the login page.")
        login_button.click()

        # Verify successful login by checking "Log out" presence
        logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        if logout_button is None:
            self.fail("Log out link is not present after login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()