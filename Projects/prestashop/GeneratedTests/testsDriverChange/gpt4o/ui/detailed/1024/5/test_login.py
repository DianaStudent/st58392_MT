from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header and footer visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Header or footer is not visible.")

        # Check for input fields
        try:
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Email or password input field is not visible.")

        # Check for buttons and links
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            forgot_password_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        except:
            self.fail("Sign in button or links (forgot password, register) are not visible.")

        # Check for navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Navigation links (home, clothes, accessories, art) are not visible.")

        # Interact with the UI components
        email_field.send_keys("test@example.com")
        password_field.send_keys("password123")
        sign_in_button.click()

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()