import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/en/')

    def test_login_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Sign in" link
        sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Sign in']]")))
        sign_in_link.click()

        # Wait for the login form to load
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))

        # Enter credentials and log in
        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")
        login_button.click()

        # Verify that "Sign out" appears, indicating a successful login
        try:
            sign_out_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sign out']")))
        except Exception as e:
            self.fail("Login failed, 'Sign out' link not found.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()