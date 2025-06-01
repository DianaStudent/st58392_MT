from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver

        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer
        footer = driver.find_element(By.CLASS_NAME, "footer")
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check input fields
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        password_input = driver.find_element(By.ID, "Password")

        self.assertTrue(email_input.is_displayed(), "Email input field is not visible")
        self.assertTrue(password_input.is_displayed(), "Password input field is not visible")

        # Check buttons
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        register_button = driver.find_element(By.CLASS_NAME, "register-button")

        self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

        # Check labels
        email_label = driver.find_element(By.XPATH, "//label[@for='Email']")
        password_label = driver.find_element(By.XPATH, "//label[@for='Password']")

        self.assertTrue(email_label.is_displayed(), "Email label is not visible")
        self.assertTrue(password_label.is_displayed(), "Password label is not visible")

        # Interact with elements
        login_button.click()
        
        # Check reaction (for demonstration purposes, checking for an element that should appear)
        error_notification = self.wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))

        self.assertTrue(error_notification.is_displayed(), "Error notification did not appear after login attempt")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()