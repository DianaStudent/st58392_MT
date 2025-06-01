import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Define WebDriverWait
        wait = WebDriverWait(driver, 20)

        # Confirm the presence of headers (checking an example header)
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        except:
            self.fail("Header 'h1' not found or not visible.")

        # Verify the presence of key links
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except:
            self.fail("One or more main navigation links ('Clothes', 'Accessories', 'Art') not found or not visible.")

        # Check presence of form fields
        driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))
        except:
            self.fail("Email or Password input field not found or not visible.")

        # Check presence of buttons
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, 'submit-login')))
        except:
            self.fail("Sign in button not found or not visible.")

        # Interact with an element, e.g., clicking sign in button
        sign_in_button.click()

        # Verify no errors in UI (assuming an error message would appear if there's an error)
        try:
            error_message = driver.find_element(By.CLASS_NAME, 'alert-danger')
            self.fail("Error message displayed after clicking the sign in button.")
        except:
            pass  # No error message found, this is expected

    def tearDown(self):
        # Close the browser instance
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()