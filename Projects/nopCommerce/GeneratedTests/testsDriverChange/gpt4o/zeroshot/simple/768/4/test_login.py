import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the correct driver path if necessary
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Click on "My account" to go to login page
        try:
            my_account_link = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//ul[@class='top-menu notmobile']//a[text()='My account']")))
            my_account_link.click()
        except Exception as e:
            self.fail("My account link not found: " + str(e))

        # Enter email
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            email_field.send_keys("admin@admin.com")
        except Exception as e:
            self.fail("Email field not found: " + str(e))

        # Enter password
        try:
            password_field = driver.find_element(By.ID, "Password")
            password_field.send_keys("admin")
        except Exception as e:
            self.fail("Password field not found: " + str(e))

        # Click Login button
        try:
            login_button = driver.find_element(By.XPATH, "//button[@class='button-1 login-button']")
            login_button.click()
        except Exception as e:
            self.fail("Login button not found: " + str(e))

        # Verify successful login by checking the presence of "Log out" link
        try:
            logout_link = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[text()='Log out']")))
            self.assertTrue(logout_link.is_displayed(), "Log out link not displayed.")
        except Exception as e:
            self.fail("Log out link not found: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()