import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_page_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header, "Header is missing")

        # Check navigation menu
        nav_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'main-menu')))
        self.assertIsNotNone(nav_menu, "Navigation menu is missing")

        # Check login form fields
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        self.assertIsNotNone(email_input, "Email input is missing")

        password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        self.assertIsNotNone(password_input, "Password input is missing")

        repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'repeatPassword')))
        self.assertIsNotNone(repeat_password_input, "Repeat password input is missing")

        # Check buttons
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
        self.assertIsNotNone(login_button, "Register button is missing")

        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertIsNotNone(accept_cookies_button, "Accept cookies button is missing")

        # Click the accept cookies button
        accept_cookies_button.click()

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer is missing")

        # Verify interaction with registration form
        first_name_input = driver.find_element(By.NAME, 'firstName')
        last_name_input = driver.find_element(By.NAME, 'lastName')
        
        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")

        # Confirm UI reacts visually (form interaction)
        self.assertEqual(first_name_input.get_attribute("value"), "John", "First name did not update")
        self.assertEqual(last_name_input.get_attribute("value"), "Doe", "Last name did not update")

if __name__ == "__main__":
    unittest.main()