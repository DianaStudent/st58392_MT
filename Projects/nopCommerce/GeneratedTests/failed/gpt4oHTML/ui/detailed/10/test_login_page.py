from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestStoreUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check header elements
        header_selector = By.CLASS_NAME, "header"
        if not self.wait.until(EC.visibility_of_element_located(header_selector)):
            self.fail("Header not visible")

        # Check footer elements
        footer_selector = By.CLASS_NAME, "footer"
        if not self.wait.until(EC.visibility_of_element_located(footer_selector)):
            self.fail("Footer not visible")

        # Check login form elements
        email_selector = By.ID, "Email"
        password_selector = By.ID, "Password"
        login_button_selector = By.CSS_SELECTOR, "button.login-button"
        if not all([
            self.wait.until(EC.visibility_of_element_located(email_selector)),
            self.wait.until(EC.visibility_of_element_located(password_selector)),
            self.wait.until(EC.visibility_of_element_located(login_button_selector)),
        ]):
            self.fail("Login form elements missing or not visible")

        # Interact with elements
        email_field = driver.find_element(*email_selector)
        password_field = driver.find_element(*password_selector)
        login_button = driver.find_element(*login_button_selector)

        # Visual feedback or interaction check
        email_field.send_keys("test@example.com")
        password_field.send_keys("testpassword")
        login_button.click()

        # Check for potential error message or success feedback (as an example post-click check)
        success_selector = By.ID, "dialog-notifications-success"
        error_selector = By.ID, "dialog-notifications-error"
        
        success_present = self.wait.until(EC.visibility_of_element_located(success_selector))
        error_present = self.wait.until(EC.visibility_of_element_located(error_selector))

        if not success_present and not error_present:
            self.fail("No feedback on post-login attempt")

if __name__ == "__main__":
    unittest.main()