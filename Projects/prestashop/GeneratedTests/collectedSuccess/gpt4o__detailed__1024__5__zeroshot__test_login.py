import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info a")))
        login_link.click()

        # Step 3: Wait for the login page to load
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))

        # Step 4: Fill in the email and password fields
        email_field.send_keys("test@user.com")
        password_field = driver.find_element(By.ID, "field-password")
        password_field.send_keys("test@user1")

        # Step 5: Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login
        sign_out_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout")))

        # Step 7: Confirm successful login
        if not sign_out_button or not sign_out_button.is_displayed():
            self.fail("Sign out button not found or not visible.")
        
        username_display = driver.find_element(By.CSS_SELECTOR, "span.hidden-sm-down")
        if not username_display or not username_display.is_displayed() or "test user" not in username_display.text:
            self.fail("Username 'test user' not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()