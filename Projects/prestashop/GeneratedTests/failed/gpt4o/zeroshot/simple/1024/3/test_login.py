from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self):
        driver = self.driver
        wait = self.wait
        
        # Click on 'Sign in' link
        sign_in_link = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        sign_in_link.click()
        
        # Enter email
        email_field = wait.until(
            EC.visibility_of_element_located((By.ID, "field-email"))
        )
        email_field.clear()
        email_field.send_keys("test@user.com")
        
        # Enter password
        password_field = wait.until(
            EC.visibility_of_element_located((By.ID, "field-password"))
        )
        password_field.clear()
        password_field.send_keys("test@user1")
        
        # Click 'Sign in' button
        sign_in_button = wait.until(
            EC.element_to_be_clickable((By.ID, "submit-login"))
        )
        sign_in_button.click()
        
        # Confirm login success by ensuring 'Sign out' is visible
        try:
            sign_out_link = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except Exception as e:
            self.fail("Login failed, 'Sign out' not visible: {}".format(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()