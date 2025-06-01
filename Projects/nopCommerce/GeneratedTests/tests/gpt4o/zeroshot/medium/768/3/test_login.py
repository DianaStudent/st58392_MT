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
        self.driver.get("http://max/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page and wait for "My account" link
        my_account = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        self.assertTrue(my_account.is_displayed(), "My account link is not visible")

        # Step 2: Click the "My account" link
        my_account.click()

        # Step 3: Wait for the login page to load
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        self.assertTrue(email_input.is_displayed(), "Email input field is not visible")
        
        password_input = driver.find_element(By.ID, "Password")
        self.assertTrue(password_input.is_displayed(), "Password input field is not visible")
        
        login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button[type='submit']")
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")

        # Step 4: Enter the email and password
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Step 5: Click the login button to submit the form
        login_button.click()

        # Step 6: Verify that the user is logged in by checking the "Log out" button
        logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        self.assertTrue(logout_link.is_displayed(), "Log out link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()