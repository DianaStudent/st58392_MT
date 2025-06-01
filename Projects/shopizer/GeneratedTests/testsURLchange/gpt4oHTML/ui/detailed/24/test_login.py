import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = self.wait

        # Ensure header is visible
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertIsNotNone(header, "Header is missing.")

        # Ensure footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertIsNotNone(footer, "Footer is missing.")

        # Check visibility of input fields on login page
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_button.click()

        # Check email input field
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        self.assertIsNotNone(email_input, "Email input field is missing.")

        # Check password input field
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'loginPassword')))
        self.assertIsNotNone(password_input, "Password input field is missing.")

        # Check login button
        login_submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Login']")))
        self.assertIsNotNone(login_submit_button, "Login submit button is missing.")

        # Check remember me checkbox
        remember_me_checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))
        self.assertIsNotNone(remember_me_checkbox, "Remember me checkbox is missing.")

        # Interact with Accept Cookies button
        accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
        accept_cookies_button.click()

        # Check main navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        self.assertIsNotNone(home_link, "Home link is missing in the navigation.")

        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        self.assertIsNotNone(tables_link, "Tables link is missing in the navigation.")

        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        self.assertIsNotNone(chairs_link, "Chairs link is missing in the navigation.")

        # Ensure UI elements react visually
        login_submit_button.click()  # Click the login button for demonstration

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()