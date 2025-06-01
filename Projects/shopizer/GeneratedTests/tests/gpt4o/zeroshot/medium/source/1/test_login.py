import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the button is present
        try:
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            print("Cookie button not found, continuing with the test.")

        # Click on the account icon
        account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_icon.click()

        # Click on the "Login" link
        login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/login']")))
        login_link.click()

        # Fill in the email field
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        if not email_field:
            self.fail("Email input not found.")
        email_field.send_keys("test2@user.com")

        # Fill in the password field
        password_field = driver.find_element(By.NAME, "loginPassword")
        if not password_field:
            self.fail("Password input not found.")
        password_field.send_keys("test**11")

        # Submit the login form
        submit_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        submit_button.click()

        # Confirm successful login by checking the URL
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        except:
            self.fail("Failed to redirect to /my-account after login.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)