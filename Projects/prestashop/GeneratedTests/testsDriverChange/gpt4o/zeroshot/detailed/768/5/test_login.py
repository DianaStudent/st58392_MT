from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "http://localhost:8080/en/"
        self.driver.get(self.url)

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info a")))
        login_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields
        email_input = driver.find_element(By.ID, "field-email")
        wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.send_keys("test@user.com")

        password_input = driver.find_element(By.ID, "field-password")
        wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.send_keys("test@user1")

        # Step 5: Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout")))

        # Step 7: Confirm that login was successful
        try:
            sign_out = driver.find_element(By.CSS_SELECTOR, "a.logout")
            assert "Sign out" in sign_out.text

            username_display = driver.find_element(By.CSS_SELECTOR, "a.account span.hidden-sm-down")
            assert "test user" in username_display.text

        except Exception as e:
            self.fail(f"Login verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()