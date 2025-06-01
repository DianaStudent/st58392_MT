import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click the login link from the top navigation.
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: Wait for the login page to load.
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields.
        email_input = driver.find_element(By.ID, "field-email")
        password_input = driver.find_element(By.ID, "field-password")
        
        email_input.clear()
        email_input.send_keys("test@user.com")
        password_input.clear()
        password_input.send_keys("test@user1")

        # Step 5: Click the submit button.
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Wait for the redirect after login.
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-info")))

        # Step 7: Confirm that login was successful
        try:
            sign_out_link = driver.find_element(By.LINK_TEXT, "Sign out")
            user_name = driver.find_element(By.XPATH, "//a[@class='account']/span")

            self.assertTrue(sign_out_link.is_displayed(), "Sign out link not displayed")
            self.assertTrue(user_name.is_displayed() and user_name.text.strip() != "", "User name not displayed")

        except Exception as e:
            self.fail(f"Login verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()