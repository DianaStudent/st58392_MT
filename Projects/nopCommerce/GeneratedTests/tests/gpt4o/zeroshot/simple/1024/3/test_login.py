import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Navigate to login page
        try:
            my_account_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My account")))
            my_account_button.click()
        except:
            self.fail("Unable to find 'My account' link.")

        # Fill the login form
        try:
            email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
            email_field.clear()
            email_field.send_keys("admin@admin.com")

            password_field = driver.find_element(By.ID, "Password")
            password_field.clear()
            password_field.send_keys("admin")
            
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.login-button")))
            login_button.click()
        except:
            self.fail("Unable to find login form elements.")

        # Confirm success by checking “Log out” button
        try:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
        except:
            self.fail("Login failed or 'Log out' button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()