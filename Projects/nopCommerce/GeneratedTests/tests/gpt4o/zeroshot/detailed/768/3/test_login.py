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
        self.driver.get("http://max/")
    
    def test_login(self):
        driver = self.driver

        # Click the "My account" link in the top navigation
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except:
            self.fail("Failed to load the home page or locate 'My account' link.")

        # Wait until the login page is fully loaded
        try:
            login_page_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome, Please Sign In!')]"))
            )
            self.assertTrue(login_page_title.is_displayed())
        except:
            self.fail("Failed to load login page.")

        # Fill in the email and password fields
        try:
            email_input = driver.find_element(By.ID, "Email")
            password_input = driver.find_element(By.ID, "Password")

            email_input.send_keys("admin@admin.com")
            password_input.send_keys("admin")
        except:
            self.fail("Email or password input fields are missing.")

        # Click the login button
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login-button")
            login_button.click()
        except:
            self.fail("Login button is missing or not clickable.")

        # Verify that the user is logged in by checking if the "Administration" link is visible
        try:
            admin_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Administration"))
            )
            self.assertTrue(admin_link.is_displayed())
        except:
            self.fail("Log in failed, 'Administration' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()