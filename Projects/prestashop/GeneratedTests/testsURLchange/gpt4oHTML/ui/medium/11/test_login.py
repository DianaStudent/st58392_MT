import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
        clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
        accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
        art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

        # Check for form fields and buttons
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))

        # Check for the presence of a forgot password link
        forgot_password_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Forgot your password?')]")))

        # Check that these elements not only exist but are visible and interactable
        self.assertTrue(home_link.is_displayed(), "Home link is not displayed")
        self.assertTrue(clothes_link.is_displayed(), "Clothes link is not displayed")
        self.assertTrue(accessories_link.is_displayed(), "Accessories link is not displayed")
        self.assertTrue(art_link.is_displayed(), "Art link is not displayed")
        self.assertTrue(email_input.is_displayed(), "Email input is not displayed")
        self.assertTrue(password_input.is_displayed(), "Password input is not displayed")
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not displayed")
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot password link is not displayed")

    def test_ui_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Interact with the email field
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        email_input.send_keys("test@example.com")

        # Interact with the password field
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        password_input.send_keys("password123")

        # Click the sign-in button
        sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
        sign_in_button.click()

        # Verify no error message on the page (example generic check for the absence of alerts)
        alerts = driver.find_elements(By.CLASS_NAME, "alert")
        if alerts:
            self.fail("Error alerts found after clicking sign in button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()