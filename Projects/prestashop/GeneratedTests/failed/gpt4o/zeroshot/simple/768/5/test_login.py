from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
    
    def test_login(self):
        driver = self.driver

        try:
            # Click on "Sign in" link
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
            
            # Fill in email
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_input.send_keys("test@user.com")
            
            # Fill in password
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys("test@user1")
            
            # Click on "Sign in" button
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "submit-login"))
            )
            sign_in_button.click()
            
            # Verify "Sign out" is visible
            sign_out_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
            )
            assert sign_out_element is not None
            
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()