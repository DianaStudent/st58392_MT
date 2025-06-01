from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver

        # Step 2: Click on the login link in the top menu.
        login_link = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        login_link.click()

        # Step 3: Wait for the login page to load.
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-form")))

        # Step 4: Fill in the email and password fields.
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "field-email"))
        )
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "field-password"))
        )
        
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Step 5: Submit the login form.
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        try:
            sign_out_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
            )
            self.assertTrue(sign_out_link.is_displayed(), "Sign out link is not displayed")
        except:
            self.fail("Login failed: 'Sign out' link was not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()