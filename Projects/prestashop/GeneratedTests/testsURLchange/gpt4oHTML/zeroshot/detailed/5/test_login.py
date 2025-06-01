import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        # Initialize the driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the homepage
        driver.get("http://localhost:8080/en/")
        
        # Step 2: Click the login link from the top navigation
        login_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info a"))
        )
        login_link.click()
        
        # Step 3: Wait for the login page to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#login-form"))
        )
        
        # Step 4: Fill in the email and password fields
        email_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#field-email"))
        )
        email_input.send_keys("test@user.com")
        
        password_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#field-password"))
        )
        password_input.send_keys("test@user1")
        
        # Step 5: Click the submit button
        submit_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button#submit-login"))
        )
        submit_button.click()
        
        # Step 6: Wait for the redirect after login
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info"))
        )
        
        # Step 7: Confirm login was successful
        try:
            sign_out_button = driver.find_element(By.CSS_SELECTOR, "a.logout")
            self.assertIn("Sign out", sign_out_button.text, "Sign out button not found after login.")
            
            user_name_display = driver.find_element(By.CSS_SELECTOR, "a.account span.hidden-sm-down")
            self.assertIn("test user", user_name_display.text.strip(), "Username not visible after login.")
        
        except:
            self.fail("Login process failed or elements not present.")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()