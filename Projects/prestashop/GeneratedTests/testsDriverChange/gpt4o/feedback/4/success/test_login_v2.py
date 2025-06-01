import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        
        # Step 2: Click the login link from the top navigation
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/en/login')]"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        # Step 3: Wait for the login page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "login-form"))
            )
        except:
            self.fail("Login form did not load properly")

        # Step 4: Fill in the email and password fields
        try:
            email_field = driver.find_element(By.ID, "field-email")
            password_field = driver.find_element(By.ID, "field-password")
            
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        except:
            self.fail("Email or password input field not found")

        # Step 5: Click the submit button
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except:
            self.fail("Submit button not found")

        # Step 6: Wait for the redirect after login
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/?mylogout=')]"))
            )
        except:
            self.fail("Login did not redirect to the expected page")

        # Step 7: Confirm that login was successful
        try:
            sign_out_button = driver.find_element(By.XPATH, "//a[contains(@href, '/?mylogout=')]")
            user_name = driver.find_element(By.XPATH, "//a[contains(@href, '/my-account')]/span[contains(text(), 'test user')]")
            
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not visible")
            self.assertTrue(user_name.is_displayed(), "User name is not visible")
        except:
            self.fail("Login was not successful, Sign out button or username is not visible")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()