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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        driver.get("http://localhost:8080/en/")

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(., 'Sign in')]")))
        login_link.click()

        # Step 3: Wait for the login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields using test credentials provided
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))

        email_field.clear()
        email_field.send_keys("test@user.com")
        password_field.clear()
        password_field.send_keys("test@user1")

        # Step 5: Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        if submit_button.is_enabled():
            submit_button.click()
        else:
            self.fail("Submit button is not enabled, cannot proceed with login.")

        # Step 6: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout')]")))

        # Step 7: Confirm that login was successful
        sign_out_button = driver.find_elements(By.XPATH, "//a[contains(@class, 'logout')]")
        user_info = driver.find_elements(By.XPATH, "//a[@class='account']/span[contains(., 'test user')]")

        if not sign_out_button or not sign_out_button[0].is_displayed():
            self.fail("Login failed: 'Sign out' button not present or not visible.")

        if not user_info or not user_info[0].is_displayed():
            self.fail("Login failed: 'test user' not visible in account section.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()