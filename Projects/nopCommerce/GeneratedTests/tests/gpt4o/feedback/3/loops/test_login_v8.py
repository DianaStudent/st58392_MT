import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        driver.get("http://max/")

        # Wait and click the "My account" link
        try:
            my_account_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception:
            self.fail("My account link not found or click failed")

        # Wait for the login form to be present
        try:
            login_form = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "form[action='/login?returnurl=%2F']"))
            )
        except Exception:
            self.fail("Login form not found")

        # Enter email and password
        try:
            email_input = driver.find_element(By.ID, "Email")
            password_input = driver.find_element(By.ID, "Password")
            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except Exception:
            self.fail("Error in entering credentials")

        # Click the login button
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
            login_button.click()
        except Exception:
            self.fail("Login button click failed")

        # Verify the "Log out" link is present
        try:
            logout_link = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".admin-header-links > a.administration"))
            )
        except Exception:
            self.fail("Log out link not found, login might have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()