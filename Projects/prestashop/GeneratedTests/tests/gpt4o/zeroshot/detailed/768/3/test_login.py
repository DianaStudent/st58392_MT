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
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        try:
            # Step 2: Click the login link from the top navigation
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(@href, 'login')]"))
            )
            sign_in_link.click()

            # Step 3: Wait for the login page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//header/h1[contains(text(), 'Log in to your account')]"))
            )

            # Step 4: Fill in the email and password fields using test credentials
            email_field = driver.find_element(By.ID, "field-email")
            email_field.clear()
            email_field.send_keys("test@user.com")

            password_field = driver.find_element(By.ID, "field-password")
            password_field.clear()
            password_field.send_keys("test@user1")

            # Step 5: Click the submit button
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()

            # Step 6: Wait for the redirect after login
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout') and contains(text(),'Sign out')]"))
            )

            # Step 7: Confirm that login was successful
            sign_out_button = driver.find_elements(By.XPATH, "//a[contains(@class, 'logout') and contains(text(),'Sign out')]")
            self.assertTrue(any(sign_out_button), "Sign out button not found or invisible after login")

            user_info = driver.find_elements(By.XPATH, "//a[contains(@class, 'account')]/span[contains(text(), 'test user')]")
            self.assertTrue(any(user_info), "User information not found or invisible after login")

        except Exception as e:
            self.fail(f"Test failed due to unexpected error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()