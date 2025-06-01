import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of navigation elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Header, footer or navigation is not visible.")

        # Check visibility of form elements
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            submit_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Email input, password input or submit button is not visible.")

        # Check visibility of links
        try:
            forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
            register_link = driver.find_element(By.LINK_TEXT, "No account? Create one here")
            if not forgot_password_link.is_displayed() or not register_link.is_displayed():
                self.fail("Forgot password or register link is not visible.")
        except:
            self.fail("Forgot password or register link is not present.")

        # Interact with a button
        try:
            submit_button.click()
        except:
            self.fail("Failed to click the submit button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()