import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class MedusaStoreLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the home page
        home_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
        self.assertTrue(home_element.is_displayed(), "Home page did not load properly.")

        # Step 2: Click the "Account" button in the right left corner.
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="nav-account-link"]')))
        account_button.click()
        
        # Step 3: Wait for the login page to load
        login_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="login-page"]')))
        self.assertTrue(login_page.is_displayed(), "Login page did not appear.")

        # Step 4: Enter the email and password using credentials
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]')))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]')))

        email_input.send_keys("user@test.com")
        password_input.send_keys("testuser")
        
        # Step 5: Click the sign-in button
        sign_in_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sign-in-button"]')))
        sign_in_button.click()
        
        # Step 6: Verify that the welcome message "Hello user" is present
        welcome_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="welcome-message"]')))
        self.assertEqual(welcome_message.get_attribute('data-value'), "user", "Login failed or welcome message is incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()