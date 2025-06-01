import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Or use another driver if needed
        self.driver.get("http://max/")
    
    def test_login(self):
        driver = self.driver
        
        # Navigate to login page
        try:
            my_account_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "My account"))
            )
            my_account_link.click()
        except Exception as e:
            self.fail("My account link not found or clickable.")

        # Fill the email and password
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )
            password_field = driver.find_element(By.ID, "Password")
            login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")
        except Exception as e:
            self.fail("Login form elements not found.")

        email_field.send_keys("admin@admin.com")
        password_field.send_keys("admin")
        login_button.click()

        # Check for successful login
        try:
            logout_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
            )
        except Exception as e:
            self.fail("Log out link not found, login unsuccessful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()