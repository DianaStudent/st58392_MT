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
        self.driver.get("http://localhost:8080/en/")
    
    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 2: Click on the login link in the top menu.
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()
        
        # Step 3: Wait for the login page to load.
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        
        # Step 4: Fill in the email and password fields.
        email_field.send_keys("test@user.com")
        
        password_field = driver.find_element(By.ID, "field-password")
        if not password_field:
            self.fail("Password field is not present on the login page.")
        password_field.send_keys("test@user1")

        # Step 5: Submit the login form.
        submit_button = driver.find_element(By.ID, "submit-login")
        if not submit_button:
            self.fail("Submit button is not present on the login page.")
        submit_button.click()
        
        # Step 6: Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        signout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        if not signout_link:
            self.fail("Sign out link is not present after login.")
        
        self.assertTrue(signout_link.is_displayed(), "Login unsuccessful: Sign out link is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()