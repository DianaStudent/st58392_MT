import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get("http://localhost:8080/en/")
        
        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='en/login']")))
        login_link.click()
        
        # Step 3: Wait for the login page to load
        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        
        # Step 4: Fill in the email and password fields using provided credentials
        email_input.send_keys("test@user.com")
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")
        
        # Step 5: Click the submit button
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()
        
        # Step 6: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.logout")))
        
        # Step 7: Confirm that login was successful
        try:
            sign_out_button = driver.find_element(By.CSS_SELECTOR, "a.logout")
            user_name = driver.find_element(By.CSS_SELECTOR, ".user-info span.hidden-sm-down")
            
            self.assertTrue(sign_out_button.is_displayed(), "Sign out button is not displayed")
            self.assertIn("test user", user_name.text, "Username not displayed correctly")
        except:
            self.fail("Login not successful or elements missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()