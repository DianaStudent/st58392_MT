import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Ensure header is visible
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertIsNotNone(header, "Header is not visible")

        # Ensure footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Ensure menu is visible
        menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-menu')))
        self.assertIsNotNone(menu, "Menu is not visible")

        # Registration form elements
        form_elements = [
            (By.ID, "FirstName"), 
            (By.ID, "LastName"), 
            (By.ID, "Email"), 
            (By.ID, "Password"),
            (By.ID, "ConfirmPassword"),
            (By.ID, "register-button")
        ]

        for by, value in form_elements:
            element = wait.until(EC.visibility_of_element_located((by, value)))
            self.assertIsNotNone(element, f"Element with {by}='{value}' is not visible")

        # Interact with UI elements
        firstname_input = driver.find_element(By.ID, "FirstName")
        firstname_input.send_keys("Test")

        lastname_input = driver.find_element(By.ID, "LastName")
        lastname_input.send_keys("User")

        email_input = driver.find_element(By.ID, "Email")
        email_input.send_keys("testuser@example.com")

        password_input = driver.find_element(By.ID, "Password")
        password_input.send_keys("password123")

        confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_input.send_keys("password123")

        # Click Register button
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()
        
        # Check for notifications
        notifications = driver.find_element(By.ID, "dialog-notifications-success")
        self.assertTrue(notifications.is_displayed(), "Success notification is not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()