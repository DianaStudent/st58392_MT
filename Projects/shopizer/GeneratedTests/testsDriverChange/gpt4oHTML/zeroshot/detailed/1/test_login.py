import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://localhost/")  # Replace with your URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        # Already done in setUp

        # Step 2: Click on the account icon/button in the top-right
        account_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_icon.click()

        # Step 3: Wait for the dropdown and click the "Login" link
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # Step 4: Wait for the login form to appear
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

        # Step 5: Fill in the username and password fields using credentials
        email_field = driver.find_element(By.NAME, "username")
        email_field.send_keys("test2@user.com")

        password_field = driver.find_element(By.NAME, "loginPassword")
        password_field.send_keys("test**11")

        # Step 6: Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        login_button.click()

        # Step 7: Wait for redirection or page update
        wait.until(EC.url_contains("/my-account"))

        # Step 8: Confirm successful login
        current_url = driver.current_url
        if not "/my-account" in current_url:
            self.fail("Login wasn't successful or redirection failed, current URL: " + current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()