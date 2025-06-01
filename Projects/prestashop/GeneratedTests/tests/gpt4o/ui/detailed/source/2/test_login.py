import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.driver.maximize_window()

    def test_page_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")
        
        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check navigation bar visibility
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation bar is not visible.")

        # Check email input field visibility
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        self.assertTrue(email_field.is_displayed(), "Email input field is not visible.")

        # Check password input field visibility
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        self.assertTrue(password_field.is_displayed(), "Password input field is not visible.")

        # Check sign-in button visibility
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        self.assertTrue(sign_in_button.is_displayed(), "Sign-in button is not visible.")

        # Check "Forgot your password?" link visibility
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot password link is not visible.")

        # Interact with elements
        sign_in_button.click()  # Example interaction with button

        # Confirm UI reacts visually (example could be checking an error message if the page reacts to the click)
        # Note: Additional steps would be required if clicking causes a new element to be visible
        # Example: wait for an error message to appear and check its visibility
        # error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-class")))
        # self.assertTrue(error_message.is_displayed(), "Error message is not visible after clicking sign-in.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()