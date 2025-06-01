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
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify "Login" link exists and click it
        login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/login')]")))
        self.assertIsNotNone(login_link, "Login link not found in the top navigation.")
        login_link.click()

        # Wait for the login page to load
        email_input = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        password_input = driver.find_element(By.ID, "Password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.login-button")
        
        # Ensure all elements are present
        self.assertIsNotNone(email_input, "Email input not found on login page.")
        self.assertIsNotNone(password_input, "Password input not found on login page.")
        self.assertIsNotNone(login_button, "Login button not found on login page.")

        # Fill in the login credentials
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click on the login button
        login_button.click()
        
        # Verify that the "Log out" button is present in the top navigation
        logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Log out')]")))
        self.assertIsNotNone(logout_button, "Login failed or 'Log out' button not found in the top navigation.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()