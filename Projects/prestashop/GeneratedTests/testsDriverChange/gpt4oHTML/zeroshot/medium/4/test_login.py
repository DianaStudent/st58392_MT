import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the login link in the top menu
        login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a/span[text()='Sign in']/parent::a")))
        login_link.click()

        # Step 2: Wait for the login page to load
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))

        # Step 3: Fill in the email and password fields
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Step 4: Submit the login form
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
        submit_button.click()

        # Step 5: Verify login was successful by checking for "Sign out" in the top bar
        try:
            sign_out_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Sign out')]")))
            self.assertIsNotNone(sign_out_link)
        except:
            self.fail("The Sign out link was not found, login may have failed.")

if __name__ == "__main__":
    unittest.main()