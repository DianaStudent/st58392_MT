import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/login")
        self.driver.maximize_window()

    def test_ui_elements_presence(self):
        driver = self.driver
        
        try:
            # Confirm the presence of navigation links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Clothes']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Accessories']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Art']"))
            )

            # Confirm the presence of form fields
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )
            
            # Confirm the presence of buttons
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "submit-login"))
            )
            show_password_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@data-action='show-password']"))
            )

            # Confirm the presence of 'Forgot your password?' link
            forgot_password_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'password-recovery')]"))
            )

            # Interact with elements
            email_input.send_keys("test@example.com")
            password_input.send_keys("password123")
            show_password_button.click()
            
            # Check that clicking 'Sign in' does not cause errors
            sign_in_button.click()

            # Visual update check (simple check)
            account_creation_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'No account? Create one here')]"))
            )
            
        except Exception as e:
            self.fail(f"Test failed due to missing element or error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()