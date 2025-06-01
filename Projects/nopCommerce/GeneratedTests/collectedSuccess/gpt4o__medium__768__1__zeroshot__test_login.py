import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.set_window_size(1920, 1080)  # Ensure elements are properly displayed at default zoom

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        try:
            home_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        except:
            self.fail("Home page did not load correctly.")
        
        # Step 2: Click the "Login" link
        home_link.click()

        # Step 3: Wait for the login page to load
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        except:
            self.fail("Login page did not load correctly.")

        # Step 4: Enter the email and password
        email_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")

        # Step 5: Click the login button to submit the form
        try:
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
            login_button.click()
        except:
            self.fail("Login button is missing or could not be clicked.")

        # Step 6: Verify that the user is logged in by checking for the "Log out" button
        try:
            logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            self.assertTrue(logout_button.is_displayed(), "Log out button is not displayed.")
        except:
            self.fail("Log out button is missing or user is not logged in.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()