import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header-menu")))

        # Step 2: Click the "Login" button in the top navigation
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
        login_link.click()

        # Step 3: Wait until the login page loads fully
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-page")))

        # Step 4: Fill in the email and password fields using the provided credentials
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))

        email_input.clear()
        email_input.send_keys("admin@admin.com")

        password_input.clear()
        password_input.send_keys("admin")

        # Step 5: Click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button is present
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        except:
            self.fail("Log out button not found. Login might have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()