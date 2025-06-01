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
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        
        # Step 2: Click on the login link
        login_link = self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Sign in")
        ))
        login_link.click()

        # Step 3: Wait for the login page to load
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[text()='Log in to your account']")
        ))

        # Step 4: Fill in the login form
        email_field = self.wait.until(EC.presence_of_element_located(
            (By.ID, "field-email")
        ))
        password_field = driver.find_element(By.ID, "field-password")
        
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Step 5: Submit the login form
        submit_button = driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Step 6: Verify that login was successful
        try:
            account_info = self.wait.until(EC.presence_of_element_located(
                (By.LINK_TEXT, "Sign out")
            ))
            self.assertTrue("Sign out" in account_info.text)
        except:
            self.fail("Login failed or 'Sign out' not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()